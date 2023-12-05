from sqlalchemy.ext.asyncio import AsyncSession

from tactic.application.common.uow import UnitOfWork


class SQLAlchemyUoW(UnitOfWork):
    """SQLAlchemy UnitOfWork implementation"""

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
