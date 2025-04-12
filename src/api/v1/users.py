from typing import List

from fastapi import APIRouter

from core.schemas.user import UserCreate
from src.core.dependencies import SessionDep
from src.core.schemas.user import UserRead
from src.crud.users import UserCRUD



router = APIRouter(tags=["Users"])


@router.get("/", response_model=List[UserRead])
async def get_users(session: SessionDep):
    return await UserCRUD.get_all_users(session=session)


@router.post("/", response_model=UserRead)
async def create_user(session: SessionDep, user_create: UserCreate):
    new_user = await UserCRUD.create_user(session, user_create)
    return new_user