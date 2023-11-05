from abc import ABC

from clean_architecture_app.domain.entities.user import User
from clean_architecture_app.domain.value_objects.user import UserId


class AbstractRepository(ABC):
    """Abstract implementation of repository"""

    def __init__(self, session) -> None:
        self.session = session


class UserRepository(AbstractRepository):
    """User repository"""

    async def create(self, user: User) -> None:
        raise NotImplementedError

    async def exists(self, user_id: UserId) -> bool:
        raise NotImplementedError
