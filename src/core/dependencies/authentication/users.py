from core.dependencies import SessionDep
from core.models import User


async def get_users_db(session: SessionDep):
    yield User.get_db(session=session)


