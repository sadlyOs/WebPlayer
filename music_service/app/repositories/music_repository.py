from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Music, Play_list
from sqlalchemy.orm import selectinload


class MusicRepository:
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def create_music(self, title: str, artist: str, album: str, genre: str, file_path: str, photo_path: str, playlist_id: int, user_id: int):
        music = Music(user_id=user_id, title=title, artist=artist, album=album, genre=genre, file_path=file_path, photo_path=photo_path, playlist_id=playlist_id)
        self.__session.add(music)
        await self.__session.commit()

    async def create_playlist(self, user_id: int, title: str, photo_path: str):
        playlist = Play_list(user_id=user_id, title=title, photo_path=photo_path)
        self.__session.add(playlist)
        await self.__session.commit()

    async def get_music_by_id(self, id: int):
        execute = await self.__session.execute(select(Music).filter(Music.id == id))
        music = execute.first()
        return music

    async def get_all_music(self, user_id: int):
        execute = await self.__session.execute(select(Music).filter(Music.user_id == user_id))
        music = execute.scalars().all()
        return music

    async def get_all_playlists(self, user_id: int):
        execute = await self.__session.execute(select(Play_list).options(selectinload(Play_list.music)).filter(Play_list.user_id == user_id))
        playlists = execute.scalars().all()
        return playlists

    async def get_playlist_by_id(self, id: int):
        execute = await self.__session.execute(select(Play_list).filter(Play_list.id == id))
        playlist = execute.scalars().all()
        return playlist

    async def delete_playlist(self, id: int):
        execute = await self.__session.execute(select(Play_list).filter(Play_list.id == id))
        playlist = execute.first()
        if playlist:
            await self.__session.delete(playlist)
            await self.__session.commit()

    async def delete_music(self, id: int):
        execute = await self.__session.execute(select(Music).filter(Music.id == id))
        music = execute.first()
        if music:
            await self.__session.delete(music)
            await self.__session.commit()

