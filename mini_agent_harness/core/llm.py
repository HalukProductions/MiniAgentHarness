"""LLM provider abstraction used by the Agent core loop.

For now supports a trivial Echo provider and optionally OpenAI Chat API if
`openai` is installed and `OPENAI_API_KEY` is set.
"""
from __future__ import annotations

import os
from typing import Protocol, runtime_checkable


@runtime_checkable
class LLM(Protocol):
    """Protocol for language model backends."""

    def generate(self, prompt: str) -> str:  # pragma: no cover
        """Return the model text completion for the given prompt."""
        ...


class EchoLLM:
    """Simplest possible provider that just echoes the prompt."""

    def generate(self, prompt: str) -> str:  # noqa: D401
        return f"[ECHO] {prompt}"


class OpenAILLM:  # pragma: no cover — requires network
    """Thin wrapper around the OpenAI chat completion endpoint."""

    def __init__(self, model: str = "gpt-3.5-turbo") -> None:
        try:
            import openai  # type: ignore
        except ModuleNotFoundError:  # pragma: no cover
            raise ImportError("openai package not installed. Run `poetry add openai`. ") from None

        if not os.getenv("OPENAI_API_KEY"):
            raise RuntimeError("OPENAI_API_KEY environment variable not set.")

        self._openai = openai
        self._model = model

    def generate(self, prompt: str) -> str:  # pragma: no cover
        completion = self._openai.ChatCompletion.create(
            model=self._model,
            messages=[{"role": "user", "content": prompt}],
        )
        # Newer openai>=1.0 might differ; adapt when upgrading.
        return completion.choices[0].message.content


_DEF_PROVIDER = "echo"  # default provider if nothing specified


def get_default_llm() -> LLM:
    """Return an LLM instance based on env vars.

    Priority order:
    1. `MINI_AGENT_LLM` env var ("openai" or "echo").
    2. If `OPENAI_API_KEY` is set → "openai".
    3. Fallback to "echo".
    """

    provider = os.getenv("MINI_AGENT_LLM") or (
        "openai" if os.getenv("OPENAI_API_KEY") else _DEF_PROVIDER
    )

    if provider == "openai":
        return OpenAILLM()

    # Default to echo
    return EchoLLM() 