# agents/mcp.py

from router import Router

class MCP:
    def __init__(self):
        self.router = Router()

    def execute(self, agent_to_execute):
        print(f"MCP: Executing agent '{agent_to_execute}'")
        self.router.route(agent_to_execute)
        print("-" * 30)