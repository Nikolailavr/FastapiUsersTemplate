from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from src.core import settings
from .users import router as users_router
from .auth import router as auth_router
from .groups import router as grops_router

http_bearer = HTTPBearer(auto_error=False)

router_v1 = APIRouter(
    prefix=settings.api.v1.prefix,
    dependencies=[Depends(http_bearer)],
)

router_v1.include_router(users_router)
router_v1.include_router(auth_router)
router_v1.include_router(grops_router)
