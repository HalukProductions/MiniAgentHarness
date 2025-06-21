from mini_agent_harness.testing import agent_fixture


quickstart_agent = agent_fixture("agents/quickstart.yaml")


def test_quickstart_echo():
    result = quickstart_agent.run("Hello")
    assert "[ECHO]" in result.response_text 