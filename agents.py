# agents/agents.py

class BaseAgent:
    def handle(self):
        print(f"{self.__class__.__name__}: handled")

AGENTS = {
    name.lower(): type(f"{name}Agent", (BaseAgent,), {})
    for name in [
        "Data", "Api", "Db", "File", "Email", "Auth", "Log", "Cache",
        "Search", "Report", "Backup", "Deploy", "Test", "Monitor", "Parse",
        "Validate", "Transform", "Notify", "Encrypt", "Sync"
    ]
}