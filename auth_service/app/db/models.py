import datetime

from sqlalchemy import ForeignKey , text

from sqlalchemy.orm import Mapped , mapped_column , relationship , DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, index = True)
    username: Mapped[str] = mapped_column(unique=True, index = True)
    email: Mapped[str] = mapped_column(unique=True, index = True)
    hash_password: Mapped[str]
    token: Mapped[str] = ""

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"

