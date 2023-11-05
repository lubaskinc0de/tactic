import asyncio
import logging

from aiogram import Bot, Dispatcher

from aiogram.fsm.storage.redis import (
    RedisStorage,
    DefaultKeyBuilder,
    RedisEventIsolation,
)

from aiogram_dialog import setup_dialogs
from sqlalchemy.ext.asyncio import async_sessionmaker

from clean_architecture_app.infrastructure.config_loader import load_config
from clean_architecture_app.infrastructure.db.main import get_async_sessionmaker, get_engine

from clean_architecture_app.presentation.telegram import register_handlers, register_dialogs

from clean_architecture_app.main.ioc import IoC


async def main():
    """Main coroutine"""

    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger("sqlalchemy.engine")
    logger.setLevel(logging.INFO)

    config = load_config()

    engine_factory = get_engine(config.db)
    engine = await anext(engine_factory)

    session_factory: async_sessionmaker = await get_async_sessionmaker(engine)

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

    try:
        await dp.start_polling(bot)
    finally:
        logging.info("Shutdown..")

        await anext(engine_factory)


if __name__ == "__main__":
    asyncio.run(main())
