from enum import Enum
from typing import Annotated

from fastapi import FastAPI, Response
import uvicorn
from app import get_all_equipment_to_csv, get_all_equipment_to_excel, maintenance_cost_sum, add_equipment

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

@app.get("/equipment/export/csv")
def export_equipment_csv():
    f = get_all_equipment_to_csv()
    return Response(content=f, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=equipment_report.csv"})

@app.get("/equipment/export/excel")
def export_equipment_excel():
    f = get_all_equipment_to_excel()
    return Response(content=f, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers={"Content-Disposition": "attachment; filename=lab_equipment_report.xlsx"})
    
if __name__== "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
