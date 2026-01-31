# UniGuru Core Extraction & Governance Alignment
**Owner: Isha Singh — UniGuru Core Team**

## Project Overview
This project focuses on identifying and isolating the **UniGuru Reasoning Core** from its surrounding "Product Shell". By defining hard boundaries and non-agentic contracts, we ensure that UniGuru can safely integrate with the Intelligence Layer (Sankalp) and Enforcement Engine (Raj) without risking hallucinated authority or accidental execution.

## Folder Structure
```text
isha_task4/
├── docs/                      # Deliverables for Micro-Builds 1-4
│   ├── 01_repo_mapping.md      # UniGuru vs Product Shell Analysis
│   ├── 02_core_definition.md   # Contract & Invariants
│   ├── 03_extraction_plan.md   # Step-by-step decoupling strategy
│   ├── 04_integration_notes.md # Demo & Misuse Safety guarantees
│   └── 05_non_goals.md         # Explicit project boundaries
├── src/
│   ├── uniguru_core/          # THE EXTRACTED CORE (Governance-First)
│   │   ├── contract.py         # IO Contracts (Pydantic-ready)
│   │   ├── reasoning.py        # Isolated reasoning logic
│   │   └── governance.py       # Invariant enforcement layer
│   └── product_shell/         # (Placeholder for existing UI/API code)
├── tests/
│   └── core_tests/            # Proof-of-Boundary verification
└── research/
    └── learning_kit/          # Mandatory Governance Exercises
```

## Key Achievements
1.  **Clean Extraction**: Reasoning logic is now a standalone module that cannot import from the shell.
2.  **Hard Invariants**: The `GovernanceEngine` prevents `sudo`, `eval`, and "authority" hallucinations.
3.  **Governance-First**: Aligned with AI Being requirements for non-agentic, read-only intelligence.

## How to Verify
Run the boundary safety tests:
```bash
python tests/core_tests/test_boundaries.py
```

## Alignment Notes
- **Sankalp**: Reasoning contract is defined in `contract.py`.
- **Raj Prajapati**: Enforcement hooks are integrated into `governance.py`.
- **Ishan/Abhishek**: Evaluator-compatible output format implemented.
