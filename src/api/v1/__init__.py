from fastapi import APIRouter

from src.core import settings
from .users import router as users_router
from .auth import router as auth_router

router_v1 = APIRouter(
    prefix=settings.api.v1.prefix,
)

router_v1.include_router(
    users_router,
    prefix=settings.api.v1.users,
)

router_v1.include_router(
    auth_router,
    prefix=settings.api.v1.auth,
)