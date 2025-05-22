# agent/main.py

from mcp import MCP

def run_tests():
    print("MCP: Starting tests...")
    test_agents = ["data", "api", "invalid", "file", "email", "SYNC"]
    mcp_instance = MCP()
    [mcp_instance.execute(agent) for agent in test_agents]
    print("MCP: Tests completed.")

if __name__ == "__main__":
    run_tests()