import datetime

from sqlalchemy import ForeignKey , text

from sqlalchemy.orm import Mapped , mapped_column , relationship
from main_models import Base


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, index = True)
    username: Mapped[str] = mapped_column(unique=True, index = True)
    email: Mapped[str] = mapped_column(unique=True, index = True)
    hash_password: Mapped[str]
    token: Mapped[str] = ""
    content: Mapped[list["Content"]] = relationship(
        back_populates="user",
    )

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"

class Content(Base):
    __tablename__ = "content"
    id: Mapped[int] = mapped_column(primary_key=True, index = True)
    title: Mapped[str]
    main_content: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default = text("TIMEZONE('utc', now())"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete = "CASCADE"))
    user: Mapped["User"] = relationship(
        back_populates="content"
    )
    def __repr__(self):
        return f"{self.title}"
