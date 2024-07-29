from fastapi import FastAPI
from auth import routers

app = FastAPI()

for router in routers:
    app.include_router(router)

