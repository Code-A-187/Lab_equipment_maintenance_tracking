from fastapi import FastAPI
import uvicorn
from app import maintenance_cost_sum, add_equipment

from pydantic import BaseModel

class EquipmentCreate(BaseModel):
    name: str
    status: str
    maintenance_cost: int

app = FastAPI(title="Lab Operations API")

@app.get("/")
def root():
    return {"message": "Lab Operations API is online"}

@app.post("/equipment/create")
def create_equipment(item: EquipmentCreate):
    msg = add_equipment(item.name, item.status, item.maintenance_cost)

    return {
        "message": msg,
        "data_recieved": item
    }

@app.get("/equipment/cost/")
def get_cost(status: str = "all"): # if we put default value becomes optional
    total = maintenance_cost_sum(status)
    return {
        "status_filter": status,
        "total_maintenance_cost": total
        }

    
if __name__== "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
