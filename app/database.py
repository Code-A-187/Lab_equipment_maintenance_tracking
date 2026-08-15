# lab_equipment_list = [
#     ("Centrifuge", "active", 500),
#     ("Universal Oven", "active", 450)
#     # {"id": 3, "name": "Balance", "status": "broken", "maintenance_cost": 530},
#     # {'id': 4, 'name': 'Furnace', 'status': 'active', 'maintenance_cost': 250}
# ]

import sqlite3
import csv
from pathlib import Path

import pandas as pd
from io import StringIO, BytesIO

# con = sqlite3.connect("lab.db")

# cur = con.cursor()

# # cur.execute("CREATE TABLE equipment(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, status TEXT, maintenance_cost INTEGER)")

# # con.close()
DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DATA_DIR / "lab.db"

def add_equipment(name, status, maintenance_cost):
    equipment = (name, status,  maintenance_cost)
    
    # # for i in lst:
    # #     if i["id"] == equipment["id"]:
    # #         return "Equipment with same ID already in the list"

    # "with" automatically commits transactions AND closes the connection
    # even if an error occurs inside the block!
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute("INSERT INTO equipment VALUES(NULL, ?, ?, ?)", equipment)
        # con.commit() is handled automatically by 'with' on exit

    return "Equipment successfully saved to database!"
    
# def list_broken_equipment(lst):
#     list_broken = []
#     for i in lst:
#         if i["status"] == "broken":
#             list_broken.append(i)
    
#     return list_broken

# def list_active_equipment(lst):
#     return [i for i in lst if i["status"] == "active"]

def maintenance_cost_sum(status):
    status = status.lower().strip()

    # total = 0
    # if status == "active":
    #     # active_list = list_active_equipment(lst)
    #     # for i in active_list:
    #     #     total += i["maintenance_cost"]
        
    # elif status == "broken":
    #     # broken_list =  list_broken_equipment(lst)
    #     # for i in broken_list:
    #     #     total += i["maintenance_cost"]

    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        if status in ["active", "broken"]:
            cur.execute("SELECT SUM(maintenance_cost) FROM equipment WHERE status = ?", [status])
        else:
            cur.execute("SELECT SUM(maintenance_cost) FROM equipment")
        # for i in lst:
        #     total += i["maintenance_cost"]
        result = cur.fetchone()[0]

    if result is None:
        return 0
    return result

def get_all_equipment_to_csv():
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute("SELECT id, name, status, maintenance_cost FROM equipment")
        result = make_CSV(cur.fetchall())
        return result

def make_CSV(data):
    data_file = StringIO()
    writer = csv.writer(data_file)
    writer.writerow(['ID', 'Name', 'Status', 'Maintenance Cost'])
    writer.writerows(data)
    return data_file.getvalue()


def get_all_equipment_to_excel():
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute("SELECT id, name, status, maintenance_cost FROM equipment")
        result = make_excel(cur.fetchall())
        return result

def make_excel(data):
    data_file = BytesIO()
    df = pd.DataFrame(data, columns=['ID', 'Name', 'Status', 'Maintenance Cost'])
    total_cost =  df['Maintenance Cost'].sum()
    df.loc[len(df)] = ['TOTAL', '', '', total_cost]
    with pd.ExcelWriter(data_file) as writer:
        df.to_excel(writer, index=False)
    return data_file.getvalue()

def get_analytics_summary():
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        
        # Triple quotes """ allow multi-line SQL without backslash syntax errors
        cur.execute("""
            SELECT 
                COUNT(*) as total_equipment_count,
                SUM(CASE WHEN status = 'active' THEN 1 ELSE 0 END) as active_count,
                SUM(CASE WHEN status = 'broken' THEN 1 ELSE 0 END) as broken_count,
                COALESCE(SUM(maintenance_cost), 0.0) as total_maintenance_cost,
                COALESCE(AVG(maintenance_cost), 0.0) as average_maintenance_cost,
                COALESCE(MAX(maintenance_cost), 0.0) as most_expensive_item_cost
            FROM equipment
        """)

        row = cur.fetchone()
        
        # Convert sqlite3.Row to a standard Python dictionary
        data = dict(row) if row else {
            "total_count": 0,
            "active_count": 0,
            "broken_count": 0,
            "total_cost": 0.0,
            "avg_cost": 0.0,
            "max_cost": 0.0
        }

        # Calculate the broken equipment ratio percentage safely

        total = data["total_equipment_count"]
        broken = data["broken_count"] or 0

        if total > 0:
            data["broken_ratio_percentage"] = round((broken / total) * 100, 2)
        else:
            data["broken_ratio_percentage"] = 0.0

        return data
    
    
# while True:
#     choice = int(input(
#         "--- LAB OPERATIONS MENU ---\n"
#         "1. Add Equipment\n"
#         "2. Calculate Maintenance Cost\n"
#         "3. Exit\n"
#         "Choose an option:"
#     ))

#     if choice == 1:
#         print(f"Enter equipment info:")
#         print(add_equipment(input("Equipment name:"), input("Equipment status (active/broken):"), int(input("Maintenance cost:"))))
    
#     elif choice == 2:
#         print(maintenance_cost_sum(input("Status (active / broken / all)")))

#     elif choice == 3:
#         print("Goodbye!")
#         con.close()
#         break

