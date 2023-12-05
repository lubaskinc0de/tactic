from contextlib import asynccontextmanager
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from tactic.application.create_user import CreateUser

from tactic.domain.services.user import UserService

from tactic.infrastructure.db.repositories.user import UserRepositoryImpl
from tactic.infrastructure.db.uow import SQLAlchemyUoW

from tactic.presentation.interactor_factory import InteractorFactory


class IoC(InteractorFactory):
    _session_factory: async_sessionmaker[AsyncSession]

    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self._session_factory = session_factory

    @asynccontextmanager
    async def create_user(self) -> AsyncIterator[CreateUser]:
        async with self._session_factory() as session:
            uow = SQLAlchemyUoW(session)
            repo = UserRepositoryImpl(session)

            yield CreateUser(
                repository=repo,
                uow=uow,
                user_service=UserService(),
            )
