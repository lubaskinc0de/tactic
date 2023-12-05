from abc import abstractmethod, ABC

from typing import AsyncContextManager

from tactic.application.create_user import CreateUser


class InteractorFactory(ABC):
    @abstractmethod
    def create_user(self) -> AsyncContextManager[CreateUser]:
        raise NotImplementedError
