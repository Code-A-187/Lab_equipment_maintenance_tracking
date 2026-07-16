lab_equipment_list = [
    {"id": 1, "name": "Centrifuge", "status": "active", "maintenance_cost":500},
    {"id": 2, "name": "Universal Oven", "status": "active", "maintenance_cost": 450},
    {"id": 3, "name": "Balance", "status": "broken", "maintenance_cost": 530}
]

def add_equipment(lst, id, name, status, maintenance_cost):
    equipment = {"id": id, "name": name, "status": status, "maintenance_cost": maintenance_cost}
    return lst.append(equipment)

def list_broken_equipment(lst):
    list_broken = []
    for i in lst:
        if i["status"] == "broken":
            list_broken.append(i)
    
    return list_broken

def maintenance_cost_sum(lst):
    total = 0
    for i in lst:
        total += i["maintenance_cost"]
    
    return total

print(add_equipment(lab_equipment_list, 4, "Furnace", "active", 250))
print(list_broken_equipment(lab_equipment_list))
print(maintenance_cost_sum(lab_equipment_list))