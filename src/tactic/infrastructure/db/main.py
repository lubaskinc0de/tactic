import logging

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from tactic.infrastructure.config_loader import DBConfig


async def get_engine(settings: DBConfig) -> AsyncGenerator[AsyncEngine, None]:
    """Get async SA engine"""

    engine = create_async_engine(
        settings.get_connection_url(),
        future=True,
    )

    logging.info("Engine is created.")

    yield engine

    await engine.dispose()

    logging.info("Engine is disposed.")


async def get_async_sessionmaker(
    engine: AsyncEngine,
) -> async_sessionmaker[AsyncSession]:
    """Get async SA sessionmaker"""

    session_factory = async_sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )

    return session_factory
