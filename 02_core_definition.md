# UniGuru Core Contract & Invariants

## 1. Core Mission
The UniGuru Core is a **read-only reasoning engine** for academic and career guidance. It must never initiate actions in the real world or modify the state of the host system.

## 2. Input Contract
The Core accepts a standard `ReasoningRequest` object:
- `query`: (string) The natural language input from the user.
- `context`: (dict) Validated metadata (e.g., student GPA, interests).
- `history`: (list) Previous *reasoning* steps (optional).

## 3. Output Contract
The Core produces a `ReasoningResponse` object:
- `reasoning`: (string) The logical chain used to reach the conclusion.
- `conclusion`: (string) The final guidance for the user.
- `metadata`: (dict) Confidence scores, source citations.
- `safety_status`: (string) `ALLOWED` | `DENIED`.

## 4. Hard Invariants (Boundary Guarantees)
The following invariants must be enforced at the code level:

1.  **Non-Agentic**: The core must never generate strings that resemble tool calls, shell commands, or SQL queries.
2.  **Stateless**: The core does not remember previous calls unless history is explicitly passed in the input contract.
3.  **Isolation**: The core cannot import modules from the `product_shell` (e.g., `db`, `auth`).
4.  **No Side-Effects**: Calling the core 100 times with the same input must not change any global state or filesystem content.

## 5. Verboten Actions (Never Do)
- **NEVER** use `eval()`, `exec()`, or `subprocess`.
- **NEVER** write to a database.
- **NEVER** use "authority" words in outputs like "I am authorized to...", "Access granted", or "Executing...".
- **NEVER** give legal or medical advice.
