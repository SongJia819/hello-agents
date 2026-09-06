import unittest
from types import SimpleNamespace

from app.services.llm_streaming import collect_streamed_answer


class StreamModel:
    def __init__(self, attempts):
        self.attempts = iter(attempts)
        self.calls = 0

    async def astream(self, _messages):
        self.calls += 1
        for text in next(self.attempts):
            yield SimpleNamespace(content=text)


class StreamingAnswerTests(unittest.IsolatedAsyncioTestCase):
    async def test_chunks_are_assembled_without_whitespace_normalization(self):
        model = StreamModel([["first ", "line\nsecond"]])
        answer = await collect_streamed_answer(model, [], agent="query", node="answer",
                                               state={"request_id": "one"}, attempts=3, fallback="fallback")
        self.assertEqual(answer, "first line\nsecond")
        self.assertEqual(model.calls, 1)

    async def test_empty_stream_retries_to_limit_then_returns_fallback(self):
        model = StreamModel([[" "], [], ["\n"]])
        answer = await collect_streamed_answer(model, [], agent="knowledge", node="answer",
                                               state={"request_id": "two"}, attempts=3, fallback="fallback")
        self.assertEqual(answer, "fallback")
        self.assertEqual(model.calls, 3)

    async def test_empty_first_attempt_uses_second_stream(self):
        model = StreamModel([[], ["answer"]])
        answer = await collect_streamed_answer(model, [], agent="knowledge", node="answer",
                                               state={"request_id": "three"}, attempts=3, fallback="fallback")
        self.assertEqual(answer, "answer")
        self.assertEqual(model.calls, 2)
