lab_equipment_list = [
    {"id": 1, "name": "Centrifuge", "status": "active", "maintenance_cost":500},
    {"id": 2, "name": "Universal Oven", "status": "active", "maintenance_cost": 450},
    {"id": 3, "name": "Balance", "status": "broken", "maintenance_cost": 530},
    {'id': 4, 'name': 'Furnace', 'status': 'active', 'maintenance_cost': 250}
]

def add_equipment(lst, name, status, maintenance_cost):
    id = max([i["id"] for i in lst]) + 1 # if some id is deleted will always get the max id
    equipment = {"id": id, "name": name, "status": status, "maintenance_cost": maintenance_cost}
    for i in lst:
        if i["id"] == equipment["id"]:
            return "Equipment with same ID already in the list"
    
    lst.append(equipment)
    return lst
    
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

print(add_equipment(lab_equipment_list, "HPLC", "broken", 450))
print(list_broken_equipment(lab_equipment_list))
print(list_active_equipment(lab_equipment_list))
print(maintenance_cost_sum(lab_equipment_list, ""))