from fastapi import APIRouter

from api.v1.fastapi_users import fastapi_users
from core import settings
from core.dependencies.authentication import authentication_backend
from core.schemas.user import (
    UserRead,
    UserCreate,
)

router = APIRouter(
    tags=["Auth"],
    prefix=settings.api.v1.auth,
)

# /login
# /logout
router.include_router(
    router=fastapi_users.get_auth_router(
        authentication_backend,
        requires_verification=True,
    ),
)


# /register
router.include_router(
    router=fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    ),
)

# /request-verify-token
# /verify
router.include_router(
    router=fastapi_users.get_verify_router(UserRead),
)

# /forgot-password
# /reset-password
router.include_router(
    router=fastapi_users.get_reset_password_router(),
)
