from datetime import datetime
from typing import Annotated

from sqlalchemy import ForeignKey , text
from sqlalchemy.orm import declarative_base , Mapped , mapped_column , relationship

Base = declarative_base()

null = Annotated[str | None, mapped_column(nullable = True)]

class Play_list(Base):
    __tablename__ = "play_list"
    id: Mapped[int] = mapped_column(primary_key = True)
    user_id: Mapped[int]
    title: Mapped[str]
    music: Mapped[list["Music"]] = relationship(back_populates = "playlist")
    upload_date: Mapped[datetime] = mapped_column(server_default = text( "TIMEZONE('utc', now())"))

class Music(Base):
    __tablename__ = "music"
    id: Mapped[int] = mapped_column(primary_key = True)
    user_id: Mapped[int]
    title: Mapped[str]
    artist: Mapped[null]
    album: Mapped[null]
    genre: Mapped[null]
    file_path: Mapped[str]
    photo_path: Mapped[str]
    upload_date: Mapped[datetime] = mapped_column(server_default = text("TIMEZONE('utc', now())"))
    playlist_id: Mapped[int] = mapped_column(ForeignKey("play_list.id", ondelete = "CASCADE"))
    playlist: Mapped["Play_list"] = relationship(back_populates = "music")

