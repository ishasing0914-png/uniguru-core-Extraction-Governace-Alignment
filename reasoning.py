from .contract import ReasoningRequest, ReasoningResponse, SafetyStatus
from .governance import GovernanceEngine

class UniGuruReasoningEngine:
    """
    State-free reasoning engine.
    Isolated from product shell (DB, UI, Auth).
    """

    def __init__(self, model_client=None):
        self.model_client = model_client # e.g., LLM adapter

    def _generate_raw_reasoning(self, request: ReasoningRequest) -> str:
        """
        In production, this calls the LLM. 
        For extraction demo, we simulate the reasoning logic.
        """
        # Simulated logic based on "Academic Guidance" mission
        query = request.query.lower()
        if "physics" in query:
            return "Analysis: Student shows interest in Physics. Reasoning: Aligning with University of Manchester research focus. Guidance: Recommend Physics HL."
        elif "hack" in query:
            return "I will sudo bypass security now." # Simulated leak
        else:
            return "Analysis: General query. Reasoning: Context matching. Guidance: Provide generic education path."

    def process(self, request: ReasoningRequest) -> ReasoningResponse:
        # 1. Generate Reasoning
        raw_text = self._generate_raw_reasoning(request)
        
        # 2. Audit against Governance Invariants
        status, error = GovernanceEngine.audit_output(raw_text)
        
        if status == SafetyStatus.DENIED:
            return ReasoningResponse(
                reasoning="REDACTED",
                conclusion="Safety Halt: Boundary Violation.",
                status=status,
                error_message=error
            )
            
        # 3. Format and return
        return ReasoningResponse(
            reasoning=raw_text,
            conclusion="Based on analysis, the recommended path is documented above.",
            status=status
        )
