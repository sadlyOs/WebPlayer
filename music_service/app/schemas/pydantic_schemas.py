from datetime import datetime

from fastapi import Form
from pydantic import BaseModel , Field


class MusicAdd(BaseModel):
    user_id: int = Form()
    title: str = Form()
    artist: str | None = Form(default=None)
    album: str | None = Form(default=None)
    genre: str | None = Form(default=None)
    playlist_id: int = Form()

class PlaylistAdd(BaseModel):
    user_id: int = Field()
    title: str = Form()


class PlaylistView(PlaylistAdd):
    id: int = Field()
    upload_date: datetime = Field(default_factory = datetime.utcnow)
    music: "MusicView"
class MusicView(MusicAdd):
    id: int = Field()
    upload_date: datetime = Field(default_factory = datetime.utcnow)