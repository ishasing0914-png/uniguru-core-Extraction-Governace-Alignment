# UniGuru vs Product Shell Mapping

## 1. Reality Check: The Current State
The existing repository consists of several layers that intertwine core reasoning with execution and presentation.

### Product Shell (To be Isolated)
These are the components that handle user interaction, session state, and infrastructure but do not contribute to the "Intelligence/Reasoning" itself.
- **UI/Frontend Layer**: All HTML, CSS, and client-side JavaScript.
- **Auth & Session**: RBAC (Role Based Access Control), JWT handling, and user session management.
- **Data Persistence**: Direct DB connectors (SQL/NoSQL) that store user history or profile metadata.
- **Execution Logic**: Scripts that send emails, trigger webhooks, or perform filesystem operations.

### UniGuru Core (The Intelligence Layer)
This is the "Reasoning Engine" that provides the unique value of UniGuru.
- **Reasoning Harness**: The logic that processes natural language and produces structured guidance.
- **Prompt Architecture**: The specific instructions and few-shot examples used to prime the LLM.
- **Retrieval Logic (RAG)**: The methods used to fetch academic context (without modifying it).
- **Safety Boundaries**: Input/Output filters that ensure non-agentic behavior.

## 2. Explicit Marking
| Component | Classification | Reasoning |
| :--- | :--- | :--- |
| `reasoning_harness.py` | **UniGuru Core** | Contains the actual logic for processing and boundary enforcement. |
| `api/routes.py` | **Product Shell** | Handles routing and HTTP overhead; should call the Core via a contract. |
| `templates/` | **Product Shell** | Pure presentation. |
| `prompt_library/` | **UniGuru Core** | Defines the reasoning behavior. |
| `db/migrations/` | **Product Shell** | Persistent state management (Execution-adjacent). |

## 3. Potential for UniGuru Core
The "Core" should be able to run in a headless environment (CLI, Lambda, or as a library) without needing a database or a web server.
