import os
import sys

from app.api.api_ import api_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.db.models import Base
from app.db.session import async_engine



app = FastAPI(openapi_url = "/auth/v1/openapi.json", docs_url="/auth/v1/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Измените на список доменов вашего фронтенда
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
@app.on_event("startup")
async def startup():
    async with async_engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()

app.include_router(api_router)




@app.get("/")
async def home():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("auth_service.main:auth_service", host="0.0.0.0", port=8000)