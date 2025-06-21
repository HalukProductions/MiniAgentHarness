from mini_agent_harness.core import Agent, AgentResult
from mini_agent_harness.testing import agent_fixture

class MockLLM:
    """Returns scripted responses for each call."""

    def __init__(self):
        self.calls = 0

    def generate(self, prompt: str) -> str:  # noqa: D401
        self.calls += 1
        if self.calls == 1:
            return "ACTION: echo\nARG: hello"
        return "FINAL: done"


def test_react_loop_invokes_tool():
    manifest = {
        "name": "react-agent",
        "description": "demo",
        "mode": "react",
        "tools": ["tools/echo.yaml"],
    }
    agent = Agent(manifest, llm=MockLLM())
    result: AgentResult = agent.run("ignored user input")
    assert result.response_text == "done" 