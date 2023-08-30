from sqlalchemy.orm import declarative_base

from sqlalchemy import Column, BigInteger

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, autoincrement=False)
