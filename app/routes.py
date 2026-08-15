from fastapi import APIRouter, FastAPI, Response
from app.database import get_all_equipment_to_csv, get_all_equipment_to_excel, get_analytics_summary, maintenance_cost_sum, add_equipment
from app.schemas import AnalyticsSummaryResponse, EquipmentCreate

router = APIRouter(prefix="/equipment", tags=["Equipment"])

@router.get("/")
def root():
    return {"msg": "Lab Operations API is online"}

@router.post("/create/")
def create_equipment(item: EquipmentCreate):
    msg = add_equipment(item.name, item.status, item.maintenance_cost)

    return {
        "message": msg,
        "data_received": item
    }

@router.get("/cost/")
def get_cost(status: str = "all"): # if we put default value becomes optional
    total = maintenance_cost_sum(status)
    return {
        "status_filter": status,
        "total_maintenance_cost": total
        }

@router.get("/export/csv")
def export_equipment_csv():
    f = get_all_equipment_to_csv()
    return Response(content=f, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=equipment_report.csv"})

@router.get("/export/excel")
def export_equipment_excel():
    f = get_all_equipment_to_excel()
    return Response(content=f, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers={"Content-Disposition": "attachment; filename=lab_equipment_report.xlsx"})

@router.get("/analytics/summary/", response_model=AnalyticsSummaryResponse)
def analytics_summary():
    data = get_analytics_summary()

    return AnalyticsSummaryResponse(**data)