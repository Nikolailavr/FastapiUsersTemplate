from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import router_v1
from core.config import settings
from core.db import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup
    yield
    #shutdown
    await db_helper.dispose()



main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)
main_app.include_router(router_v1, prefix=settings.api.prefix)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
