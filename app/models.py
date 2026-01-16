from .database import Base, engine
from sqlalchemy import Column, Integer, String


class UserSchema(Base):
    __tablename__ = "user_schema"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)


Base.metadata.create_all(bind = engine)