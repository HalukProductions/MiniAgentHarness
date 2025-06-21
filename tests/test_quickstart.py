from mini_agent_harness.testing import agent_fixture


quickstart_agent = agent_fixture("agents/quickstart.yaml")


def test_quickstart_echo():
    # direct llm path
    result = quickstart_agent.run("Hello")
    assert "[ECHO]" in result.response_text


def test_tool_invocation():
    result = quickstart_agent.run("echo: hi there")
    assert result.response_text == "hi there" 