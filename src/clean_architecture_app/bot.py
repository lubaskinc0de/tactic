import asyncio
import logging

from aiogram import Bot, Dispatcher

from aiogram.fsm.storage.redis import (
    RedisStorage,
    DefaultKeyBuilder,
    RedisEventIsolation,
)
from aiogram_dialog import setup_dialogs

from infrastructure.config_loader import load_config, DBConfig

from presentation.telegram import register_handlers, register_dialogs

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from ioc import IoC


async def get_async_sessionmaker(db_config: DBConfig) -> async_sessionmaker:
    """Get async sessionmaker instance"""

    engine = create_async_engine(
        db_config.get_connection_url(),
        future=True,
    )

    session_factory = async_sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )

    return session_factory


async def main():
    """Main coroutine"""

    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger("sqlalchemy.engine")
    logger.setLevel(logging.INFO)

    config = load_config()

    session_factory: async_sessionmaker = await get_async_sessionmaker(config.db)

    ioc = IoC(session_factory=session_factory)

    token = config.bot.api_token
    bot = Bot(token=token, parse_mode="html")

    storage: RedisStorage = RedisStorage.from_url(
        "redis://bot_redis:6379", key_builder=DefaultKeyBuilder(with_destiny=True)
    )

    dp = Dispatcher(
        storage=storage,
        events_isolation=RedisEventIsolation(redis=storage.redis),
        ioc=ioc,
    )

    register_handlers(dp)
    register_dialogs(dp)

    setup_dialogs(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
