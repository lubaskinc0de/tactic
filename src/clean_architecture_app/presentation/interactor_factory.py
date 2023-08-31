from abc import abstractmethod, ABC

from typing import AsyncContextManager

from application.create_user.use_case import CreateUser


class InteractorFactory(ABC):
    @abstractmethod
    async def create_user(self) -> AsyncContextManager[CreateUser]:
        raise NotImplementedError
