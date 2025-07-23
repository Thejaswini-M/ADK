from models import InputData, Suggestion

class OptimizationAgent:
    def __init__(self):
        self.agent_id = "lca-optimizer"

    def process(self, data: LCAData) -> Suggestion:
        # mocked up response
        return Suggestion(
            crate_id=data.crate_id,
            suggested_lca_value=120,
            reason="Replace foam type X with foam type Y",
            suggested_material_id="FOAM-Y"
        )
