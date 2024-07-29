from fastapi import APIRouter

from auth.register import router
routers: list[APIRouter] = [router]