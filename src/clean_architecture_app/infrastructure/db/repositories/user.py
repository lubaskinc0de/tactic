from sqlalchemy import select, exists

from clean_architecture_app.infrastructure.db import models

from clean_architecture_app.application.common.repositories import UserRepository

from clean_architecture_app.domain.entities.user import User
from clean_architecture_app.domain.value_objects.user import UserId


class UserRepositoryImpl(UserRepository):
    """Database abstraction layer"""

    async def create(self, user: User) -> None:
        user: models.User = models.User(
            user_id=user.user_id,
        )

        self.session.add(user)

    async def exists(self, user_id: UserId) -> bool:
        q = select(exists().where(models.User.user_id == user_id))

        res = await self.session.execute(q)

        return res.scalar()
