from app.repositories.music_repository import MusicRepository
from fastapi import UploadFile

from app.utils.aws import AWS
from app.utils.jwt_token import JWT

class MusicService:
    def __init__(self, music_repository: MusicRepository):
        self.__music_repository = music_repository

    async def create_music(self, user_id: int, title: str, artist: str, album: str, genre: str, file_path: str, photo_path: str, playlist_id: int):
        await self.__music_repository.create_music(user_id=user_id, title=title, artist=artist, album=album, genre=genre, playlist_id=playlist_id, file_path=file_path, photo_path=photo_path, )

    async def create_playlist(self, user_id: int, title: str, photo_path: str):
        await self.__music_repository.create_playlist(user_id = user_id, title=title, photo_path = photo_path)

    async def add_data_to_buckets(self, file: UploadFile, data: dict, bucket_name: str):
        if bucket_name == "musicbasket":
            await AWS.upload_file(file = file.file , file_name = f"{data['title']}.mp3", bucket_name = bucket_name)
        else:
            await AWS.upload_file(file = file.file , file_name = f"{data['title']}_{data['user_id']}.jpg", bucket_name = bucket_name)



    async def get_music_by_id(self, id: int):
        return await self.__music_repository.get_music_by_id(id)

    async def get_all_music(self, user_id: int):
        return await self.__music_repository.get_all_music(user_id=user_id)

    async def get_all_playlists(self, user_id: int):
        return await self.__music_repository.get_all_playlists(user_id = user_id)

    async def get_playlist_by_id(self, id: int):
        return await self.__music_repository.get_playlist_by_id(id)

    async def delete_playlist(self, id: int):
        await self.__music_repository.delete_playlist(id)
    async def delete_music(self, id: int):
        await self.__music_repository.delete_music(id)

    async def delete_file(self, file_name: str, bucket_name: str):
        await AWS.delete_file(file_name = file_name, bucket_name = bucket_name)

    async def get_hwt_operation(self):
        return JWT