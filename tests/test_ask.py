from types import SimpleNamespace

from app import ask


def test_ask_prints_input_and_output_token_counts(monkeypatch, capsys):
    response = SimpleNamespace(
        text="answer",
        usage_metadata=SimpleNamespace(
            prompt_token_count=12,
            candidates_token_count=7,
        ),
    )

    class FakeModels:
        def generate_content(self, **kwargs):
            return response

    class FakeClient:
        models = FakeModels()

    monkeypatch.setattr(ask.genai, "Client", lambda api_key: FakeClient())
    monkeypatch.setattr(ask, "get_api_key", lambda: "test-key")

    assert ask.ask("question") == "answer"
    assert capsys.readouterr().out.strip() == (
        "[usage] input_tokens=12 output_tokens=7"
    )