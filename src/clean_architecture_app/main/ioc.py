from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import async_sessionmaker

from clean_architecture_app.application.create_user.use_case import CreateUser

from clean_architecture_app.domain.services.user import UserService

from clean_architecture_app.infrastructure.db.repositories.user import UserRepositoryImpl
from clean_architecture_app.infrastructure.db.uow import SQLAlchemyUoW

from clean_architecture_app.presentation.interactor_factory import InteractorFactory


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
