import asyncio
import logging

from aiogram import Bot, Dispatcher

from aiogram.fsm.storage.redis import (
    RedisStorage,
    DefaultKeyBuilder,
    RedisEventIsolation,
)

from aiogram_dialog import setup_dialogs

from tactic.infrastructure.config_loader import load_config
from tactic.infrastructure.db.main import get_async_sessionmaker, get_engine

from tactic.presentation.telegram import register_handlers, register_dialogs

from tactic.presentation.ioc import IoC


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger("sqlalchemy.engine")
    logger.setLevel(logging.INFO)

    config = load_config()

    engine_factory = get_engine(config.db)
    engine = await anext(engine_factory)

    session_factory = await get_async_sessionmaker(engine)

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

        try:
            await anext(engine_factory)
        except StopAsyncIteration:
            logging.info("Exited")


if __name__ == "__main__":
    asyncio.run(main())
