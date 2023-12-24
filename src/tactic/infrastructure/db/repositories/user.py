from typing import Optional

from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from tactic.infrastructure.db import models

from tactic.application.common.repositories import UserRepository

from tactic.domain.entities.user import User
from tactic.domain.value_objects.user import UserId


class UserRepositoryImpl(UserRepository):
    """Database abstraction layer"""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: User) -> User:
        self.session.add(user)
        return user

    async def exists(self, user_id: UserId) -> bool:
        q = select(exists().where(models.User.user_id == user_id.to_raw()))

        res = await self.session.execute(q)

        is_exists: Optional[bool] = res.scalar()

        if not is_exists:
            is_exists = False

        return is_exists
