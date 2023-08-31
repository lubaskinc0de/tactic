from pydantic import (
    BaseModel,
)

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = ".env"
ENV_FILE_ENCODING = "utf-8"


class BotConfig(BaseSettings):
    """Bot config"""

    model_config = SettingsConfigDict(
        env_file=ENV_FILE, env_file_encoding=ENV_FILE_ENCODING, extra="ignore"
    )

    api_token: str


class BaseDBConfig(BaseSettings):
    """Base Database Connection config"""

    db_host: str
    db_name: str
    db_user: str
    db_pass: str

    model_config = SettingsConfigDict(
        env_file=ENV_FILE, env_file_encoding=ENV_FILE_ENCODING, extra="ignore"
    )

    def get_connection_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}/{self.db_name}"


class DBConfig(BaseDBConfig):
    """Database config"""


class Config(BaseModel):
    """App config"""

    bot: BotConfig
    db: DBConfig


class AlembicDB(BaseDBConfig):
    """
    Alembic database config

    need other user for migrations in production.
    """


def load_config() -> Config:
    """Get app config"""

    return Config(bot=BotConfig(), db=DBConfig())


def load_alembic_settings() -> AlembicDB:
    """Get alembic settings"""

    return AlembicDB()
