#!/usr/bin/env python3
"""Train a response-only Alpaca SFT LoRA adapter for Qwen.

Imports that can load model backends remain inside training functions so that
``--dry-run`` and the focused unit tests do not download model weights.
"""

from __future__ import annotations

import argparse
import json
import platform
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

DATASET_ID = "tatsu-lab/alpaca"
DATASET_SPLIT = "train"
TRAIN_EXAMPLE_COUNT = 1_000
DEFAULT_MODEL_ID = "Qwen/Qwen3.5-0.8B"
IGNORE_INDEX = -100


@dataclass(frozen=True)
class TrainingConfig:
    model_id: str
    output_dir: str
    max_seq_length: int
    num_train_epochs: float
    per_device_train_batch_size: int
    gradient_accumulation_steps: int
    learning_rate: float
    seed: int
    lora_r: int
    lora_alpha: int
    lora_dropout: float
    lora_target_modules: str
    bf16: bool
    fp16: bool
    gradient_checkpointing: bool


@dataclass(frozen=True)
class SelectedAlpacaDataset:
    records: Any
    source_records_scanned: int
    empty_outputs_skipped: int


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-id", default=DEFAULT_MODEL_ID)
    parser.add_argument(
        "--output-dir", default="agenticRL/outputs/qwen3.5-0.8b-alpaca-lora"
    )
    parser.add_argument("--max-seq-length", type=int, default=1024)
    parser.add_argument("--num-train-epochs", type=float, default=1.0)
    parser.add_argument("--per-device-train-batch-size", type=int, default=1)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=8)
    parser.add_argument("--learning-rate", type=float, default=2e-4)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--lora-r", type=int, default=16)
    parser.add_argument("--lora-alpha", type=int, default=32)
    parser.add_argument("--lora-dropout", type=float, default=0.05)
    parser.add_argument(
        "--lora-target-modules",
        default="q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj",
    )
    parser.add_argument("--bf16", action="store_true")
    parser.add_argument("--fp16", action="store_true")
    parser.add_argument("--gradient-checkpointing", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def config_from_args(args: argparse.Namespace) -> TrainingConfig:
    if args.max_seq_length < 1:
        raise ValueError("--max-seq-length must be positive")
    if args.per_device_train_batch_size < 1:
        raise ValueError("--per-device-train-batch-size must be positive")
    if args.gradient_accumulation_steps < 1:
        raise ValueError("--gradient-accumulation-steps must be positive")
    if args.bf16 and args.fp16:
        raise ValueError("Choose only one of --bf16 and --fp16")
    return TrainingConfig(
        model_id=args.model_id,
        output_dir=args.output_dir,
        max_seq_length=args.max_seq_length,
        num_train_epochs=args.num_train_epochs,
        per_device_train_batch_size=args.per_device_train_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.learning_rate,
        seed=args.seed,
        lora_r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        lora_target_modules=args.lora_target_modules,
        bf16=args.bf16,
        fp16=args.fp16,
        gradient_checkpointing=args.gradient_checkpointing,
    )


def load_alpaca_train_dataset() -> SelectedAlpacaDataset:
    """Select the first 1,000 non-empty Alpaca outputs in source order."""
    from datasets import load_dataset

    dataset = load_dataset("tatsu-lab/alpaca")
    train_split = dataset[DATASET_SPLIT]
    selected_indices: list[int] = []
    empty_outputs_skipped = 0
    source_records_scanned = 0
    for index, record in enumerate(train_split):
        source_records_scanned = index + 1
        if not str(record.get("output") or "").strip():
            empty_outputs_skipped += 1
            continue
        selected_indices.append(index)
        if len(selected_indices) == TRAIN_EXAMPLE_COUNT:
            return SelectedAlpacaDataset(
                records=train_split.select(selected_indices),
                source_records_scanned=source_records_scanned,
                empty_outputs_skipped=empty_outputs_skipped,
            )

    valid_count = len(selected_indices)
    if valid_count < TRAIN_EXAMPLE_COUNT:
        raise ValueError(
            f"{DATASET_ID!r} {DATASET_SPLIT!r} has {valid_count} valid records; "
            f"{TRAIN_EXAMPLE_COUNT} are required."
        )
    raise AssertionError("unreachable: successful selection returns from the loop")


def format_alpaca_prompt(record: Mapping[str, Any]) -> str:
    instruction = str(record["instruction"]).strip()
    input_text = str(record.get("input") or "").strip()
    if not instruction:
        raise ValueError("Alpaca record has an empty instruction")
    if input_text:
        return (
            "Below is an instruction that describes a task, paired with an input "
            "that provides further context. Write a response that appropriately "
            "completes the request.\n\n"
            f"### Instruction:\n{instruction}\n\n"
            f"### Input:\n{input_text}\n\n"
            "### Response:\n"
        )
    return (
        "Below is an instruction that describes a task. Write a response that "
        "appropriately completes the request.\n\n"
        f"### Instruction:\n{instruction}\n\n"
        "### Response:\n"
    )


def _token_ids(tokenizer: Any, text: str) -> list[int]:
    encoded = tokenizer(text, add_special_tokens=False)
    input_ids = encoded["input_ids"]
    return list(input_ids)


def build_tokenized_example(
    record: Mapping[str, Any], tokenizer: Any, max_seq_length: int
) -> dict[str, list[int]]:
    """Create one causal-LM example with prompt tokens excluded from loss."""
    if max_seq_length < 1:
        raise ValueError("max_seq_length must be positive")
    response = str(record["output"]).strip()
    if not response:
        raise ValueError("Alpaca record has an empty output")
    if tokenizer.eos_token is None:
        raise ValueError("Tokenizer must define an EOS token")

    prompt_ids = _token_ids(tokenizer, format_alpaca_prompt(record))
    response_ids = _token_ids(tokenizer, f"{response}{tokenizer.eos_token}")
    response_ids = response_ids[:max_seq_length]
    prompt_budget = max(0, max_seq_length - len(response_ids))
    prompt_ids = prompt_ids[-prompt_budget:] if prompt_budget else []
    input_ids = prompt_ids + response_ids
    return {
        "input_ids": input_ids,
        "attention_mask": [1] * len(input_ids),
        "labels": [IGNORE_INDEX] * len(prompt_ids) + response_ids,
    }


class ResponseOnlyDataCollator:
    """Pads causal-LM examples while preserving prompt masking in labels."""

    def __init__(self, tokenizer: Any) -> None:
        self.tokenizer = tokenizer

    def __call__(self, features: Sequence[Mapping[str, Sequence[int]]]) -> Mapping[str, Any]:
        import torch

        padded = self.tokenizer.pad(
            [
                {
                    "input_ids": list(feature["input_ids"]),
                    "attention_mask": list(feature["attention_mask"]),
                }
                for feature in features
            ],
            padding=True,
            return_tensors="pt",
        )
        max_length = padded["input_ids"].shape[1]
        labels = [
            list(feature["labels"]) + [IGNORE_INDEX] * (max_length - len(feature["labels"]))
            for feature in features
        ]
        padded["labels"] = torch.tensor(labels, dtype=torch.long)
        return padded


def _require_training_dependencies() -> tuple[Any, ...]:
    try:
        from peft import LoraConfig, TaskType, get_peft_model
        from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments, set_seed
    except ImportError as error:
        raise RuntimeError(
            "Training dependencies are missing. Install agenticRL/requirements.txt "
            "after installing a suitable PyTorch build."
        ) from error
    return AutoModelForCausalLM, AutoTokenizer, LoraConfig, TaskType, get_peft_model, Trainer, TrainingArguments, set_seed


def package_versions() -> dict[str, str]:
    from importlib.metadata import version

    versions: dict[str, str] = {"python": sys.version.split()[0], "platform": platform.platform()}
    for package in ("torch", "transformers", "datasets", "peft", "accelerate"):
        try:
            versions[package] = version(package)
        except Exception:  # Package metadata is supplementary run information.
            versions[package] = "unavailable"
    return versions


def run_dry_run() -> int:
    selection = load_alpaca_train_dataset()
    dataset = selection.records
    prompts = [format_alpaca_prompt(dataset[index]) for index in range(len(dataset))]
    if any("### Response:\n" not in prompt for prompt in prompts):
        raise RuntimeError("Alpaca prompt validation failed: response marker missing")
    with_input = sum(bool(str(dataset[index].get("input") or "").strip()) for index in range(len(dataset)))
    print(
        "Dry run passed: "
        f"dataset={DATASET_ID} split={DATASET_SPLIT} selected={len(dataset)} "
        f"scanned={selection.source_records_scanned} "
        f"skipped_empty_output={selection.empty_outputs_skipped} "
        f"with_input={with_input} without_input={len(dataset) - with_input}. "
        "No model weights were loaded and no optimizer steps were run."
    )
    return 0


def train(config: TrainingConfig) -> None:
    (
        AutoModelForCausalLM,
        AutoTokenizer,
        LoraConfig,
        TaskType,
        get_peft_model,
        Trainer,
        TrainingArguments,
        set_seed,
    ) = _require_training_dependencies()
    set_seed(config.seed)
    selection = load_alpaca_train_dataset()
    dataset = selection.records
    tokenizer = AutoTokenizer.from_pretrained(config.model_id)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"
    tokenized_dataset = dataset.map(
        lambda record: build_tokenized_example(record, tokenizer, config.max_seq_length),
        remove_columns=dataset.column_names,
        desc="Tokenizing Alpaca SFT examples",
    )
    model = AutoModelForCausalLM.from_pretrained(config.model_id)
    model.config.pad_token_id = tokenizer.pad_token_id
    if config.gradient_checkpointing:
        model.config.use_cache = False
        model.gradient_checkpointing_enable()
    target_modules = [item.strip() for item in config.lora_target_modules.split(",") if item.strip()]
    model = get_peft_model(
        model,
        LoraConfig(
            task_type=TaskType.CAUSAL_LM,
            r=config.lora_r,
            lora_alpha=config.lora_alpha,
            lora_dropout=config.lora_dropout,
            target_modules=target_modules,
        ),
    )
    trainable_parameters = sum(parameter.numel() for parameter in model.parameters() if parameter.requires_grad)
    if trainable_parameters == 0:
        raise RuntimeError("LoRA configuration produced no trainable adapter parameters")
    print(f"Trainable LoRA parameters: {trainable_parameters:,}")

    output_dir = Path(config.output_dir)
    training_args = TrainingArguments(
        output_dir=str(output_dir),
        do_train=True,
        num_train_epochs=config.num_train_epochs,
        per_device_train_batch_size=config.per_device_train_batch_size,
        gradient_accumulation_steps=config.gradient_accumulation_steps,
        learning_rate=config.learning_rate,
        seed=config.seed,
        data_seed=config.seed,
        bf16=config.bf16,
        fp16=config.fp16,
        gradient_checkpointing=config.gradient_checkpointing,
        logging_steps=10,
        save_strategy="epoch",
        save_total_limit=1,
        report_to="none",
        remove_unused_columns=False,
    )
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        data_collator=ResponseOnlyDataCollator(tokenizer),
    )
    metrics = trainer.train().metrics
    output_dir.mkdir(parents=True, exist_ok=True)
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    (output_dir / "training_args.json").write_text(
        json.dumps(asdict(config), indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    summary = {
        "base_model": config.model_id,
        "dataset": DATASET_ID,
        "split": DATASET_SPLIT,
        "selected_examples": len(dataset),
        "source_records_scanned": selection.source_records_scanned,
        "empty_outputs_skipped": selection.empty_outputs_skipped,
        "seed": config.seed,
        "trainable_lora_parameters": trainable_parameters,
        "metrics": metrics,
        "package_versions": package_versions(),
    }
    (output_dir / "run_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8"
    )
    print(f"Saved LoRA adapter, tokenizer, and run metadata to {output_dir}")


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    if args.dry_run:
        return run_dry_run()
    try:
        config = config_from_args(args)
        train(config)
    except (RuntimeError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
