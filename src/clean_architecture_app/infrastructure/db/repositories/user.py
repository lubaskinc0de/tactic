from sqlalchemy import select, exists

from infrastructure.db.repositories.abstract import AbstractSQLAlchemyRepository
from infrastructure.db import models

from domain.entities.user import User
from domain.entities.user_id import UserId


class UserRepositoryImpl(AbstractSQLAlchemyRepository):
    """Database abstraction layer"""

    async def create_user(self, user: User) -> None:
        user: models.User = models.User(
            user_id=user.user_id,
        )

        self.session.add(user)

    async def is_user_exists(self, user_id: UserId) -> bool:
        q = select(exists().where(models.User.user_id == user_id))

        res = await self.session.execute(q)

        return res.scalar()
