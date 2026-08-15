from fastapi import APIRouter, FastAPI
import uvicorn

from app.routes import router



app = FastAPI(
    title="Lab Operations API",
    description="Backend service for laboratory equipment management and analytics",
    version="1.0.0"
    )

app.include_router(router)

if __name__== "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
