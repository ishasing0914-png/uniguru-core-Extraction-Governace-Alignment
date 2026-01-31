# Explicit Non-Goals List

To ensure the UniGuru Core remains a pure reasoning engine, the following are strictly **OUT OF SCOPE**:

1.  **Refactoring existing UI**: We are not fixing the React/HTML layout.
2.  **Improving LLM Accuracy**: We are not "tuning" the model to be smarter; we are "bounding" the model to be safer.
3.  **Adding "Agentic" Planning**: No "Auto-GPT" style loops where the core decides its own next steps.
4.  **Learning / Fine-Tuning**: No Reinforcement Learning from Human Feedback (RLHF) inside the core. It is a static reasoning module.
5.  **Integration with External APIs**: The Core does not talk to external university APIs. It receives university context as an input.
6.  **Performance Optimization of the Shell**: We are not fixing "slow" login pages or DB queries.
7.  **Replacing the Enforcement Engine**: We provide the *contract* for the enforcement engine to work with, but we don't build the entire global enforcement system here.
