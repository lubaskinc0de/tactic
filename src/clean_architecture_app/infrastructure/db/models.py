from sqlalchemy.orm import declarative_base, Mapped

from sqlalchemy import Column, BigInteger

from clean_architecture_app.domain.entities.user_id import UserId

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[UserId] = Column(BigInteger, primary_key=True, autoincrement=False)
