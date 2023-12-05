from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from sqlalchemy import BigInteger

from tactic.domain.value_objects.user import UserId


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[UserId] = mapped_column(
        BigInteger, primary_key=True, autoincrement=False
    )
