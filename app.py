# lab_equipment_list = [
#     ("Centrifuge", "active", 500),
#     ("Universal Oven", "active", 450)
#     # {"id": 3, "name": "Balance", "status": "broken", "maintenance_cost": 530},
#     # {'id': 4, 'name': 'Furnace', 'status': 'active', 'maintenance_cost': 250}
# ]

import sqlite3

con = sqlite3.connect("lab.db")

cur = con.cursor()

# cur.execute("CREATE TABLE equipment(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, status TEXT, maintenance_cost INTEGER)")

# con.close()

def add_equipment(name, status, maintenance_cost):
    equipment = (name, status,  maintenance_cost)
    # # for i in lst:
    # #     if i["id"] == equipment["id"]:
    # #         return "Equipment with same ID already in the list"

    cur.execute("INSERT INTO equipment VALUES(NULL, ?, ?, ?)", equipment)
    con.commit()
    return "Equipment successfully saved to database!"
    
def list_broken_equipment(lst):
    list_broken = []
    for i in lst:
        if i["status"] == "broken":
            list_broken.append(i)
    
    return list_broken

def list_active_equipment(lst):
    return [i for i in lst if i["status"] == "active"]

def maintenance_cost_sum(lst, status):
    total = 0
    if status == "active":
        active_list = list_active_equipment(lst)
        for i in active_list:
            total += i["maintenance_cost"]
    elif status == "broken":
        broken_list =  list_broken_equipment(lst)
        for i in broken_list:
            total += i["maintenance_cost"]
    else:
        for i in lst:
            total += i["maintenance_cost"]

    return total



while True:
    choice = int(input(
        "--- LAB OPERATIONS MENU ---\n"
        "1. Add Equipment\n"
        "2. Calculate Maintenance Cost\n"
        "3. Exit\n"
        "Choose an option:"
    ))

    if choice == 1:
        print(f"Enter equipment info:")
        print(add_equipment(input("Equipment name:"), input("Equipment status (active/broken):"), input("Maintenance cost:")))
    
    elif choice == 2:
        print(maintenance_cost_sum(input("Status (active / broken / all)")))

    elif choice == 3:
        print("Goodbye!")
        con.close()
        break

