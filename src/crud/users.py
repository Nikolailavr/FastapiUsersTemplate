from sqlalchemy import select, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from core.schemas.user import UserCreate


class UserCRUD:
    @staticmethod
    async def get_all_users(
            session: AsyncSession
    ) -> Sequence[User]:
        stmt = select(User).order_by(User.id)
        result = await session.scalars(stmt)
        return result.all()

    @staticmethod
    async def create_user(
            session: AsyncSession,
            user_create: UserCreate
    ) -> User:
        user = User(**user_create.model_dump())
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
