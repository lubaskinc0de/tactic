from dataclasses import dataclass

from clean_architecture_app.application.common.use_case import UseCase
from clean_architecture_app.application.common.uow import UnitOfWork
from clean_architecture_app.application.common.repositories import UserRepository

from clean_architecture_app.domain.entities.user import User
from clean_architecture_app.domain.value_objects.user import UserId
from clean_architecture_app.domain.services.user import UserService


@dataclass
class NewUserDTO:
    user_id: UserId


class CreateUser(UseCase[NewUserDTO, UserId]):
    def __init__(
            self,
            repository: UserRepository,
            user_service: UserService,
            uow: UnitOfWork,
    ):
        self.repository = repository
        self.user_service = user_service
        self.uow = uow

    async def __call__(self, data: NewUserDTO) -> UserId:
        user: User = self.user_service.create_user(data.user_id)

        user_exists: bool = await self.repository.exists(data.user_id)

        if not user_exists:
            await self.repository.create(user)
            await self.uow.commit()

        return user.user_id
