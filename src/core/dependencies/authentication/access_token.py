from core.dependencies import SessionDep
from core.models import AccessToken


async def get_access_tokens_db(session: SessionDep):
    yield AccessToken.get_db(session=session)
