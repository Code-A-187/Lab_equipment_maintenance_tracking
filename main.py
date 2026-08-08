from enum import Enum
from typing import Annotated

from fastapi import FastAPI
import uvicorn
from app import maintenance_cost_sum, add_equipment

from pydantic import BaseModel, NonNegativeFloat, StringConstraints

class EquipentStatus(str, Enum):
    ACTIVE = "active"
    BROKEN = "broken"

class EquipmentCreate(BaseModel):
    name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=2)]
    status: EquipentStatus
    maintenance_cost: NonNegativeFloat

app = FastAPI(title="Lab Operations API")

@app.get("/")
def root():
    return {"msg": "Lab Operations API is online"}

@app.post("/equipment/create")
def create_equipment(item: EquipmentCreate):
    msg = add_equipment(item.name, item.status, item.maintenance_cost)

    return {
        "message": msg,
        "data_received": item
    }

@app.get("/equipment/cost/")
def get_cost(status: str = "all"): # if we put default value becomes optional
    total = maintenance_cost_sum(status)
    return {
        "status_filter": status,
        "total_maintenance_cost": total
        }

    
if __name__== "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
