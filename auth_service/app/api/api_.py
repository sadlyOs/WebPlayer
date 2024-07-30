from fastapi import APIRouter
from .v1 import endpoints
api_router = APIRouter()

api_router.include_router(
    endpoints.router,
    prefix = "/auth/v1",
    tags = ["API v1 Authentication and Registration"],
)