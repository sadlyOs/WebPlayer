import loguru
from fastapi import FastAPI
from app.api.api_ import api_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(openapi_url="/music/v1/openapi.json", docs_url="/music/v1/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Измените на список доменов вашего фронтенда
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# @app.on_event("startup")
# async def startup_tasks():
#     loguru.logger.info("Initializing database connection...")
#     loguru.logger.info(("Database connection established.")

app.include_router(api_router)
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

