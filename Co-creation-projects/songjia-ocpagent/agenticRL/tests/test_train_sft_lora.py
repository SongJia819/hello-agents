from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import train_sft_lora as training


class FakeDataset(list):
    @property
    def column_names(self):
        return ["instruction", "input", "output"]

    def select(self, indices):
        return FakeDataset([self[index] for index in indices])


class FakeTokenizer:
    eos_token = "<eos>"

    def __call__(self, text, add_special_tokens=False):
        return {"input_ids": [ord(character) for character in text]}


class TrainingPreparationTests(unittest.TestCase):
    def test_load_alpaca_selects_exactly_first_thousand_valid_records(self):
        records = FakeDataset(
            {"instruction": f"instruction {index}", "input": "", "output": "answer"}
            for index in range(1_001)
        )

        def fake_loader(dataset_id):
            self.assertEqual(dataset_id, "tatsu-lab/alpaca")
            return {"train": records}

        with patch("datasets.load_dataset", fake_loader):
            selection = training.load_alpaca_train_dataset()

        selected = selection.records
        self.assertEqual(len(selected), 1_000)
        self.assertEqual(selected[0]["instruction"], "instruction 0")
        self.assertEqual(selected[-1]["instruction"], "instruction 999")
        self.assertEqual(selection.source_records_scanned, 1_000)
        self.assertEqual(selection.empty_outputs_skipped, 0)

    def test_load_alpaca_backfills_an_empty_output_from_the_next_record(self):
        records = FakeDataset(
            {
                "instruction": f"instruction {index}",
                "input": "",
                "output": "" if index == 284 else "answer",
            }
            for index in range(1_001)
        )

        with patch("datasets.load_dataset", lambda _: {"train": records}):
            selection = training.load_alpaca_train_dataset()

        self.assertEqual(len(selection.records), 1_000)
        self.assertNotIn("instruction 284", [record["instruction"] for record in selection.records])
        self.assertEqual(selection.records[-1]["instruction"], "instruction 1000")
        self.assertEqual(selection.source_records_scanned, 1_001)
        self.assertEqual(selection.empty_outputs_skipped, 1)

    def test_load_alpaca_rejects_short_train_split(self):
        with patch("datasets.load_dataset", lambda _: {"train": FakeDataset()}):
            with self.assertRaisesRegex(ValueError, "has 0 valid records; 1000 are required"):
                training.load_alpaca_train_dataset()

    def test_prompt_omits_input_section_when_input_is_empty(self):
        prompt = training.format_alpaca_prompt(
            {"instruction": "Say hi", "input": "", "output": "Hi"}
        )

        self.assertNotIn("### Input:", prompt)
        self.assertIn("### Instruction:\nSay hi", prompt)
        self.assertTrue(prompt.endswith("### Response:\n"))

    def test_prompt_includes_non_empty_input_section(self):
        prompt = training.format_alpaca_prompt(
            {"instruction": "Translate", "input": "hello", "output": "hola"}
        )

        self.assertIn("### Input:\nhello", prompt)
        self.assertTrue(prompt.endswith("### Response:\n"))

    def test_tokenized_example_masks_prompt_tokens_and_keeps_response_tokens(self):
        tokenizer = FakeTokenizer()
        record = {"instruction": "Say hi", "input": "", "output": "Hi"}

        example = training.build_tokenized_example(record, tokenizer, max_seq_length=512)
        prompt_length = len(training._token_ids(tokenizer, training.format_alpaca_prompt(record)))
        response_ids = training._token_ids(tokenizer, "Hi<eos>")

        self.assertEqual(
            example["labels"][:prompt_length], [training.IGNORE_INDEX] * prompt_length
        )
        self.assertEqual(example["labels"][prompt_length:], response_ids)
        self.assertEqual(len(example["input_ids"]), len(example["labels"]))
