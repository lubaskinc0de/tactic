from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import async_sessionmaker

from application.create_user.use_case import CreateUser

from domain.services.user import UserService

from infrastructure.db.repositories.user import UserRepositoryImpl
from infrastructure.db.uow import SQLAlchemyUoW

from presentation.interactor_factory import InteractorFactory


class IoC(InteractorFactory):
    _session_factory: async_sessionmaker

    def __init__(self, session_factory: async_sessionmaker):
        self._session_factory = session_factory

    @asynccontextmanager
    async def create_user(self) -> CreateUser:
        async with self._session_factory() as session:
            uow = SQLAlchemyUoW(session)
            repo = UserRepositoryImpl(session)

            yield CreateUser(
                repository=repo,
                uow=uow,
                user_service=UserService(),
            )
