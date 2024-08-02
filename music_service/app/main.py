import loguru
from fastapi import FastAPI
from app.api.api_ import api_router

app = FastAPI()


# @app.on_event("startup")
# async def startup_tasks():
#     loguru.logger.info("Initializing database connection...")
#     loguru.logger.info(("Database connection established.")

app.include_router(api_router)
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

