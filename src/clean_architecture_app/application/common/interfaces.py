from typing import Protocol

from clean_architecture_app.domain.entities.user import User
from clean_architecture_app.domain.entities.user_id import UserId


class UnitOfWork(Protocol):
    """UoW interface"""

    async def commit(self) -> None:
        raise NotImplementedError

    async def rollback(self) -> None:
        raise NotImplementedError


class UserRepository(Protocol):
    """User repository interface"""

    async def create_user(self, user: User) -> None:
        raise NotImplementedError

    async def is_user_exists(self, user_id: UserId) -> bool:
        raise NotImplementedError
