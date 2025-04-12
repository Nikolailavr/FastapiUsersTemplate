from sqlalchemy import select, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from core.schemas.users import UserCreate


class UserCRUD:
    @staticmethod
    async def get_all_users(
            session: AsyncSession
    ) -> Sequence[User]:
        stmt = select(User).order_by(User.id)
        result = await session.scalars(stmt)
        return result.all()

