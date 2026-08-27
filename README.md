# 🔬 Lab Equipment Maintenance & Operations API

A production-ready, containerized FastAPI backend designed to automate laboratory equipment tracking, validate operational data, calculate aggregate maintenance analytics, and export business reports in CSV and Excel formats.

---

## 🚀 Key Features

* **Equipment Lifecycle Tracking:** Full CRUD endpoints for laboratory instruments with dynamic status management (`active`, `broken`).
* **Strict Input Validation:** Powered by Pydantic schemas to reject invalid entries (e.g., negative maintenance costs or empty machine names) with clear `422 Unprocessable Entity` responses.
* **Automated Data Seeding:** Pre-populates the database with realistic scientific equipment (HPLC, Spectrometers, Centrifuges) on startup.
* **In-Memory File Exports:** High-performance CSV and binary Excel (`.xlsx`) report streaming built with `pandas` and `openpyxl` without disk IO bottlenecks.
* **SQL Aggregate Analytics:** Computes overall maintenance totals, average costs, top vendor expenditures, and equipment status ratios.
* **Automated Test Suite:** Comprehensive `pytest` integration test coverage for all endpoints and validation boundaries.

---

## 🛠️ Tech Stack

* **Framework:** FastAPI (Python)
* **Database:** SQLite with persistent Docker volume mapping
* **Data Validation:** Pydantic
* **Reporting:** Pandas / openpyxl / CSV streaming
* **Testing:** Pytest & HTTPX (`TestClient`)
* **Containerization:** Docker & Docker Compose

---

## ⚙️ Quickstart Guide

### 1. Clone the Repository

```git clone https://github.com/Code-A-187/test_project_1.git```
```cd test_project_1```
``` docker-compose up --build```


#### The API automatically runs database migrations and seeds initial equipment data upon container startup

## Service Map & API EndpointsAPI Base URL: 
## 🗺️ Service Map & API Endpoints

* **API Base URL:** `http://localhost:8000`
* **Interactive Docs (Swagger):** `http://localhost:8000/docs/`

### Key Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Health check route |
| `POST` | `/equipment/create` | Add new equipment (with Pydantic validation) |
| `GET` | `/equipment/cost/` | Query equipment costs filtered by status |
| `GET` | `/equipment/analytics/summary` | Fetch SQL aggregated metrics and ratios |
| `GET` | `/equipment/export/csv` | Download lab equipment data as a `.csv` file |
| `GET` | `/equipment/export/excel` | Download formatted `.xlsx` report with summary stats |

---

## 🧪 Running Automated Tests

### To run the full `pytest` integration suite inside your Docker environment:

```docker run --rm test_project_1 pytest -v ```

### Or run locally (with active virtual environment):

```pytest -v```

## 💾 Database Persistence:
### All data persists inside a Docker volume (test_project_1_lab_data) mapped to SQLite's lab.db. Your dataset remains intact across container restarts and updates.
---