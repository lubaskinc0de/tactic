from application.common.use_case import UseCase

from domain.entities.user import User
from domain.entities.user_id import UserId

from domain.services.user import UserService

from .dto import NewUserDTO

from infrastructure.db.repositories.user import UserRepository

from application.common.interfaces import UnitOfWork


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

    def __call__(self, data: NewUserDTO) -> UserId:
        user: User = self.user_service.create_user(data.user_id)

        user_exists: bool = await self.repository.is_user_exists(data.user_id)

        if not user_exists:
            await self.repository.create_user(user)
            await self.uow.commit()

        return user.user_id
