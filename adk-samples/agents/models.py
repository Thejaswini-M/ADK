from pydantic import BaseModel
from typing import Dict

class LCAData(BaseModel):
    crate_id: str
    original_lca_value: float
    material_composition: Dict[str, float]

class OptimizationSuggestion(BaseModel):
    crate_id: str
    suggested_lca_value: float
    reason: str
    suggested_material_id: str
