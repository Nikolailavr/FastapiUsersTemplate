from fastapi import APIRouter

from api.v1.fastapi_users import fastapi_users
from core.config import settings
from core.schemas.user import (
    UserRead,
    UserUpdate,
)

router = APIRouter(
    tags=["Users"],
    prefix=settings.api.v1.users
)

# /me
# /{id}
router.include_router(
    router=fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)