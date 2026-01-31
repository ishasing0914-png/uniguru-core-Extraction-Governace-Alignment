# Demo & Misuse Safety: Behavior Guarantees

## 1. Risk Analysis
In a demo environment, there is a temptation to "make the AI look smart" by giving it more control. This creates:
- **Hallucinated Authority**: The AI claiming it can "apply for you".
- **Execution Creep**: Demo scripts that actually create test database entries.
- **Agentic Interpretation**: The AI trying to "plan" a sequence of actions.

## 2. Safety Guarantees (The "UniGuru + AI Being" Shield)

### Guarantee 1: The "Non-Action" Prefix
Every output from the Core should strictly adhere to a "guidance-only" tone. It should never use verbs like "I will", "I am doing", or "Done". It should use "You could", "I recommend", or "The logic suggests".

### Guarantee 2: String Sanitization (Static)
The extraction path includes a mandatory `BoundaryFilter`. This filter scans LLM outputs for "Action Sequences" (e.g., shell commands, JSON tool calls) and blocks them before they reach the execution engine.

### Guarantee 3: Transparent Reasoning
Instead of a "Black Box" answer, UniGuru provides a "Reasoning Trace". This exposes *why* the advice is being given, which helps the user (and the Enforcement Engine) verify that no "hidden" actions are being planned.

## 3. Demo-Safe Mocking
If the demo needs to show "Success", the Core should return a `ReasoningResponse` that says: "I recommend you click the 'Apply' button in the dashboard."
It should **NOT** return: `{"action": "click_button", "id": "apply"}`.

## 4. Misuse Prevention
Even if a user (or Sankalp's Intelligence Layer) tries to force the core into "Execution Mode" by prompting it to "Act as a linux terminal", the Hard Invariants in `uniguru_core/governance.py` will detect the `sudo` or `bash` patterns and return a `DENIED` status.
