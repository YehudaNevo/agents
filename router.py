# agents/router.py

from agents import AGENTS, BaseAgent

class Router:
    def __init__(self):
        self.agents = {k: v() for k, v in AGENTS.items()}

    def route(self, agent_name_to_call):
        agent_instance = self.agents.get(agent_name_to_call.lower(), BaseAgent())
        agent_instance.handle()