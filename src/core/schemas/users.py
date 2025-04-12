from fastapi_users import schemas

from core.types.user_id import UserIdType


class UserRead(schemas.BaseUser[UserIdType]):
    ...

class UserCreate(schemas.BaseUserCreate):
    ...

class UserUpdate(schemas.BaseUserUpdate):
    ...