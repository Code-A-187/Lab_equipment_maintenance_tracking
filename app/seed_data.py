import sqlite3
from pathlib import Path

equipment_list = [
    ("PCR machine", "active" , 200),
    ("HPLC", "active", 300),
    ("GC-MS", "active", 500),
    ("UV-VIS spectromether", "broken", 50),
    ("ICH climate chamber", "active", 80),
    ("Rotary Centrifuge", "active", 60),
    ("ICP-MS", "active", 100),
    ("IR spectromether", "broken", 95),
    ("Microscope", "active", 30),
    ("CO2 Incubator", "broken", 85),
    ("Magnetic stirrer", "active", 5),
    ("Magnetic strirrer 1", "broken", 10),
    ("Rotary evaporator", "active", 25),
    ("Laboratory refigerator", "active", 20),
    ("Freeze dryer", "active", 85),
    ("Incubator 32 litres", "active", 100),
    ("Incubator 110 litres", "active", 50),
    ("Universal oven 110 litres", "active", 40)
    ]


DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DATA_DIR / "lab.db"


def seed_data_in_DB(equipment_list):

    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS equipment")
        cur.execute("CREATE TABLE equipment(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, status TEXT, maintenance_cost INTEGER)")
        cur.executemany("INSERT INTO equipment VALUES (NULL, ?, ?, ?)", equipment_list)

    return "Equipment list successfully saved to database!"

if __name__ == "__main__":
    result = seed_data_in_DB(equipment_list)
    print(result)