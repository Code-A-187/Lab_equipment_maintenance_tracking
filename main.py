from fastapi import FastAPI
import uvicorn
import sqlite3
from app import maintenance_cost_sum, add_equipment


app = FastAPI(title="Test project")

@app.get("/")
def root():
    return {"message": "Lab Operations API is online"}

@app.post("/equipment/create")
def create_equipment():
    pass

@app.get("/equipment/cost/")
def get_cost(status: str): # if we put default value becomes optional
    con = sqlite3.connect("lab.db", check_same_thread=False)
    cur = con.cursor()

    status = status.lower().strip()
    if status in ["active", "broken"]:
        cur.execute("SELECT SUM(maintenance_cost) FROM equipment WHERE status = ?", [status])
    else:
        cur.execute("SELECT SUM(maintenance_cost) FROM equipment")
            # for i in lst:
            #     total += i["maintenance_cost"]
    result = cur.fetchone()[0]
    if result is None:
            con.close()
            return "No equipment records found."
    elif status in ["active", "broken"]:
        con.close()
        return f"Maintenance cost for all the {status} equipment is {result}"
    else:
        con.close()
        return f"Total maintenance cost is {result}"

    
if __name__== "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
