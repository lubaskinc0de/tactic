from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession


class AbstractSQLAlchemyRepository(ABC):
    """Abstract implementation of repository with SQLAlchemy session"""

    session: AsyncSession

    def __init__(self, session: AsyncSession) -> None:
        self.session = session
