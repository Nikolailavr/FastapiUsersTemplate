from typing import Annotated

from fastapi import Depends
from fastapi_users import FastAPIUsers

from core.models import User
from core.types.user_id import UserIdType

from core.dependencies.authentication import get_user_manager
from core.dependencies.authentication import authentication_backend

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)

current_active_user = fastapi_users.current_user(active=True)
current_active_superuser = fastapi_users.current_user(active=True, superuser=True)

CurrentUserDep = Annotated[User, Depends(current_active_user)]
CurrentSuperUserDep = Annotated[User, Depends(current_active_superuser)]
