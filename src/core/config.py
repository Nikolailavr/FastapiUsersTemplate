import logging
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from uvicorn.config import LOGGING_CONFIG

BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DEFAULT_FORMAT = (
    "[%(asctime)s] | %(module)20s:%(lineno)-3d | %(levelname)-8s - %(message)s"
)


class LoggingConfig(BaseModel):
    log_level: Literal[
        "debug",
        "info",
        "warning",
        "error",
        "critical",
    ] = "info"
    log_format: str = LOG_DEFAULT_FORMAT

    @property
    def log_level_value(self) -> int:
        return logging.getLevelNamesMapping()[self.log_level.upper()]

    @property
    def fastapi_config(self) -> dict:
        fastapi_cfg = LOGGING_CONFIG
        fastapi_cfg['formatters']['access']['fmt']=self.log_format
        fastapi_cfg['formatters']['default']['fmt']=self.log_format
        return fastapi_cfg


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class APIPrefixV1(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"
    auth: str = "/auth"
    groups: str = "/groups"


class APIPrefix(BaseModel):
    prefix: str = "/api"
    v1: APIPrefixV1 = APIPrefixV1()

    @property
    def bearer_token_url(self) -> str:
        # api/v1/auth/login
        parts = (self.prefix, self.v1.prefix, self.v1.auth, "/login")
        path = "".join(parts)
        return path.removeprefix("/")


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    max_overflow: int = 10
    pool_size: int = 5

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(
            BASE_DIR / ".env.template",
            BASE_DIR / ".env",
        ),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    run: RunConfig = RunConfig()
    api: APIPrefix = APIPrefix()
    logging: LoggingConfig = LoggingConfig()
    db: DatabaseConfig
    access_token: AccessToken


# try:
settings = Settings()
# except ValidationError as exc:
#     print(repr(exc.errors()[0]['type']))
