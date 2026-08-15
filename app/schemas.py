
from typing import Annotated
from enum import Enum
from pydantic import BaseModel, NonNegativeFloat, StringConstraints



class EquipentStatus(str, Enum):
    ACTIVE = "active"
    BROKEN = "broken"

class EquipmentCreate(BaseModel):
    name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=2)]
    status: EquipentStatus
    maintenance_cost: NonNegativeFloat

class AnalyticsSummaryResponse(BaseModel):
    total_equipment_count: int
    active_count: int
    broken_count: int
    broken_ratio_percentage: float
    total_maintenance_cost: float
    average_maintenance_cost: float
    most_expensive_item_cost: float