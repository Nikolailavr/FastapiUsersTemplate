from fastapi_users import schemas

from core.types.user_id import UserIdType

class UserFull:
    phone: str = ""
    name: str = ""


class UserRead(schemas.BaseUser[UserIdType], UserFull):
    ...

class UserCreate(schemas.BaseUserCreate):
    ...

class UserUpdate(schemas.BaseUserUpdate, UserFull):
    ...
