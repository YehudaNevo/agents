# Project: "AgenSys-Core" - A Minimalist & Scalable Agent System

## 🚀 Vision

AgenSys-Core aims to be an **ultra-lightweight, highly modular, and scalable agent-based system**. It's designed from the ground up with a "less is more" philosophy, prioritizing clean architecture and minimal code to achieve complex tasks through coordinated, specialized agents. The system will eventually support advanced functionalities like LLM integration, dynamic task decomposition, and persistent memory, all while adhering to its core principle of simplicity and clarity.

The ultimate goal is to create a foundational framework where developers can rapidly prototype, deploy, and scale sophisticated agentic workflows with minimal boilerplate and maximum transparency.

---
## 🏛️ Core Architecture (Target State)

The system will evolve from its current minimalist structure to a more feature-rich, yet still clean, architecture:

1.  **Master Control Program (MCP) / Orchestrator:**
    * **Entry Point:** Receives initial tasks or goals from users or external systems (e.g., via a REST API, CLI, or scheduled events).
    * **Task Decomposition (Future):** For complex tasks, the MCP (or a dedicated `PlannerAgent`) will be responsible for breaking them down into smaller, manageable sub-tasks. This might involve LLM-driven planning.
    * **Workflow Management:** Oversees the execution of tasks across multiple agents, managing dependencies and control flow.
    * **State Tracking:** Maintains the overall state of active tasks and workflows.

2.  **Router Agent:**
    * **Intelligent Routing:** Evolves beyond simple name-based routing. It will leverage context, task type, and potentially LLM-based intent recognition to direct tasks to the most appropriate agent or sequence of agents.
    * **Dynamic Agent Invocation:** Capable of discovering and invoking agents, whether they are statically defined or dynamically loaded.

3.  **Agents:**
    * **Specialized Units:** Each agent will have a clearly defined, single responsibility (e.g., `DataProcessingAgent`, `FileAccessAgent`, `APICallAgent`, `NotificationAgent`).
    * **Standardized Interface:** Agents will adhere to a common interface (e.g., a `handle(task_details)` method and a standardized message/task format).
    * **Mock & Real Implementations:** The system will always support easy swapping between mock agents (for testing and development) and real, functional agents.
    * **LLM-Powered Agents (Future):** Certain agents will encapsulate LLM interactions for specific tasks like natural language understanding, content generation, or decision-making.

4.  **Message Bus / Communication Protocol (Implicit to Explicit):**
    * Currently, communication is via direct method calls and simple parameter passing.
    * **Future:** For more complex inter-agent communication, especially asynchronous tasks or distributed agents, a lightweight message bus or a more formal message-passing protocol might be introduced. This will be done without sacrificing minimalism if possible.

5.  **Memory / State Management:**
    * **Short-Term Memory:** Context within a single task or workflow execution.
    * **Long-Term Memory (Future):** A dedicated `MemoryAgent` or service will allow agents to persist and recall information across sessions, potentially using vector databases or simple key-value stores for efficiency.

6.  **Configuration & Registry:**
    * **Centralized Agent Registry:** A clear way to define and register available agents and their configurations (as currently in `agents.py` with the `AGENTS` dictionary).
    * **Environment Management:** Secure handling of API keys and other sensitive configurations.

---
## ✨ Key Principles

* **Extreme Minimalism:** Every line of code must justify its existence. No boilerplate, no unnecessary abstractions.
* **Clean Code:** Self-documenting through clear naming and structure. Comments used only for highly complex or non-obvious logic (which should be rare in this design).
* **Modularity & Single Responsibility:** Each component (MCP, Router, individual Agents) has one job and does it well. Components should be easily replaceable or updatable.
* **Portability:** Minimal external dependencies. The core system should be runnable in various environments with ease.
* **Scalability:** The architecture should allow for adding many more agents, handling more complex tasks, and potentially distributing parts of the system without a full rewrite.
* **Testability:** Clear separation of concerns and simple interfaces will facilitate straightforward unit and integration testing.

---
## 💡 Future Enhancements (The Roadmap)

1.  **Phase 1: Foundation (Current State)**
    * Ultra-minimal MCP, Router, and dynamically generated mock Agents. ✅
    * Basic CLI test runner. ✅

2.  **Phase 2: Basic Task Handling & Real Agents**
    * Formalize `task_details` parameter passing.
    * Implement a few "real" (non-mock) utility agents (e.g., `FileReadAgent`, `SimpleApiAgent`).
    * Introduce basic error handling and reporting within the agent flow.

3.  **Phase 3: API Interface & Configuration**
    * Expose MCP functionality via a simple Flask/FastAPI REST API.
    * Implement a `.env` based configuration for API keys and settings.
    * Refine agent registration to support more complex initializations if needed.

4.  **Phase 4: First LLM Integration**
    * Introduce an `LLMAgent` or an `LLMService` for basic text generation or intent understanding.
    * Potentially enhance the `RouterAgent` to use LLM for smarter routing based on natural language tasks.
    * Ensure LLM usage is modular and can be enabled/disabled or mocked.

5.  **Phase 5: Advanced Agent Capabilities & Memory**
    * Develop more sophisticated agents (e.g., `PlannerAgent`, `WebScraperAgent`).
    * Implement a basic `MemoryAgent` for persistent storage and retrieval of information.
    * Explore simple asynchronous task handling if beneficial.

6.  **Phase 6: Tool Usage & Complex Workflows**
    * Formalize a "tool usage" pattern where agents can leverage other agents or external services as tools.
    * Enable the MCP/Orchestrator to manage multi-step workflows with dependencies between agent tasks.

---
## 🛠️ Current Project Structure (Minimal Base)