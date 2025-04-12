from typing import List

from fastapi import APIRouter

from core.schemas.users import UserCreate
from src.core.dependencies import SessionDep
from src.core.schemas.users import UserRead
from src.crud.users import UserCRUD



router = APIRouter(tags=["Users"])


@router.get("/", response_model=List[UserRead])
async def get_users(session: SessionDep):
    return await UserCRUD.get_all_users(session=session)
