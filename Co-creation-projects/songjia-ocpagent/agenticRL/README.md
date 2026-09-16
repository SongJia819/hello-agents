# Alpaca SFT + LoRA baseline

This directory provides a small, local supervised fine-tuning baseline. It
uses the Hugging Face Datasets API to load `tatsu-lab/alpaca`, selects the
first 1,000 records with non-empty outputs from its `train` split (skipping an
empty output and continuing in source order), and trains a LoRA adapter for
`Qwen/Qwen3.5-0.8B` by default. It does not interact with the OCP-agent
backend, MCP, or an OpenShift cluster.

## Setup

Install a PyTorch build that matches the local CPU or CUDA environment, then
install the remaining dependencies:

```bash
python -m pip install -r agenticRL/requirements.txt
```

The script downloads the named dataset and base model through Hugging Face when
they are absent from the standard Hugging Face cache. The dataset is published
under CC BY-NC 4.0; review its terms before using it.

## Verify data preparation

This command loads and validates the first 1,000 Alpaca records but does not
load Qwen weights, start an optimizer, or create an adapter:

```bash
python agenticRL/train_sft_lora.py --dry-run
```

## Train

The default output directory is `agenticRL/outputs/qwen3.5-0.8b-alpaca-lora`.
It receives adapter-only PEFT weights, tokenizer assets, `training_args.json`,
and `run_summary.json`; it does not normally receive a full base-model copy.

```bash
python agenticRL/train_sft_lora.py \
  --output-dir agenticRL/outputs/qwen3.5-0.8b-alpaca-lora \
  --num-train-epochs 1 \
  --per-device-train-batch-size 1 \
  --gradient-accumulation-steps 8 \
  --bf16
```

Use `--fp16` instead of `--bf16` only on suitable CUDA hardware. To reduce
memory use further, lower `--max-seq-length` or the per-device batch size. The
full job's duration and memory use depend on the installed PyTorch build and
hardware.

## Serve the LoRA adapter with vLLM

For service deployment, vLLM owns the Qwen model and GPU inference while an
application such as LangChain calls its OpenAI-compatible HTTP API. The
adapter is selected by the request model name `alpaca-lora`; use the base model
name only when the unmodified Qwen behavior is required.

Install a vLLM build compatible with the local CUDA driver and Python
environment:

```bash
python -m pip install vllm
```

From the repository root, start vLLM with this adapter. The adapter was trained
with LoRA rank 16, so `--max-lora-rank 16` avoids reserving unnecessary memory.

```bash
ADAPTER_DIR="$(pwd)/agenticRL/outputs/qwen3.5-0.8b-alpaca-lora"

vllm serve Qwen/Qwen3.5-0.8B \
  --enable-lora \
  --max-lora-rank 16 \
  --max-loras 1 \
  --dtype bfloat16 \
  --lora-modules "{\"name\": \"alpaca-lora\", \"path\": \"${ADAPTER_DIR}\", \"base_model_name\": \"Qwen/Qwen3.5-0.8B\"}"
```

Confirm that the service has registered both the base model and adapter:

```bash
curl http://localhost:8000/v1/models
```

The fine-tuning script uses the Alpaca prompt format. Use the same format with
the completions endpoint during initial evaluation, and select the adapter by
setting `model` to `alpaca-lora`:

```bash
curl http://localhost:8000/v1/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "alpaca-lora",
    "prompt": "Below is an instruction that describes a task. Write a response that appropriately completes the request.\\n\\n### Instruction:\\nExplain what LoRA is.\\n\\n### Response:\\n",
    "max_tokens": 256,
    "temperature": 0
  }'
```

For a fixed production adapter, load it at server startup as above. vLLM also
offers runtime adapter loading, but its adapter management endpoints must be
restricted to trusted administrators and never exposed to untrusted callers.
