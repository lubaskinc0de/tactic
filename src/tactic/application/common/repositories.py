from typing import Protocol

from tactic.domain.entities.user import User
from tactic.domain.value_objects.user import UserId


class UserRepository(Protocol):
    """User repository interface"""

    async def create(self, user: User) -> User:
        raise NotImplementedError

    async def exists(self, user_id: UserId) -> bool:
        raise NotImplementedError
