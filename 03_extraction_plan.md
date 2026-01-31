# Extraction & Isolation Plan

## 1. Objective
Decouple the reasoning logic from the product infrastructure to allow the Core to sit safely behind an "AI Being" layer and an "Enforcement Engine".

## 2. Step-by-Step Path

### Phase 1: Directory Decoupling
1.  Initialize `src/uniguru_core/` as a standalone Python package.
2.  Identify all reasoning-specific logic currently in the repo (e.g., prompt strings, response parsers).
3.  Move these files to `src/uniguru_core/`.

### Phase 2: Dependency Sanitization
1.  Audit `uniguru_core` imports.
2.  **REPLACE** any circular dependencies on the shell (e.g., if the prompt engine imports the User model for context, refactor it to accept context as a raw dict).
3.  Create a separate `requirements.txt` for the core (minimal dependencies: `pydantic`, `re`, `json`).

### Phase 3: The Contract Layer
1.  Implement `contract.py` using Pydantic models to strictly enforce the inputs and outputs defined in `docs/02_core_definition.md`.
2.  Wrap the main reasoning flow in a `UniGuruCore` class that acts as the single entry point.

### Phase 4: Integration Hook
1.  In the `product_shell` (e.g., `main.py`), replace old reasoning calls with the new isolated package.
2.  Introduce the `Enforcement Engine` hook: all Core outputs must pass through the `enforce_boundaries()` check before reaching the UI.

## 3. Deployment Topology
The Core can be deployed as:
- A private Python package.
- A sidecar container.
- An AWS Lambda / Google Cloud Function.
This ensures that even if the web server is compromised, the "Reasoning Agent" cannot be forced into execution mode because it lacks the necessary libraries.
