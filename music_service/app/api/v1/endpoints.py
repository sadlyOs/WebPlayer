from typing import Annotated

import loguru
from app.schemas.pydantic_schemas import MusicAdd , MusicView, PlaylistAdd, PlaylistView

from fastapi import APIRouter , Depends , UploadFile , File , Form
from fastapi.security import OAuth2PasswordBearer


from app.services.music_service import MusicService
from app.api.v1.dependencies import get_music_services
from app.utils.aws import AWS

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/auth/v1/login")

@router.post("/create")
async def create_music(
        service: Annotated[MusicService, Depends(get_music_services)],
        file: Annotated[UploadFile, File(media_type = "audio/mpeg")],
        photo: Annotated[UploadFile, File(media_type = "image/jpeg")],
        items: Annotated[MusicAdd, Depends()],
        security: Annotated[dict, Depends(oauth2_scheme)]
        ):
    loguru.logger.info(file)
    data = items.model_dump()
    loguru.logger.info(data)
    await service.add_data_to_buckets(file = file, data = data, bucket_name = "musicbasket")
    await service.add_data_to_buckets(file = photo, data = data, bucket_name = "music-photos")
    await service.create_music( **data ,
                                file_path = f"https://musicbasket.s3.eu-north-1.amazonaws.com/{data['title']}.mp3" ,
                                photo_path = f"https://music-photos.s3.eu-north-1.amazonaws.com/{data['title']}.jpg" )
    return f'Der Track "{data.get("title")}" wurde erfolgreich hochgeladen'

@router.post("/playlist")
async def create_playlist(
        service: Annotated[MusicService, Depends(get_music_services)],
        photo: Annotated[UploadFile, File(media_type = "image/jpeg")],
        items: Annotated[PlaylistAdd, Depends()],
        security: Annotated[dict, Depends(oauth2_scheme)],
):
    jwt = await service.get_hwt_operation()
    await jwt.decode_access_token( security )
    data = items.model_dump()
    loguru.logger.info(data)
    await service.add_data_to_buckets( file = photo , data = data , bucket_name = "playlistphotos" )
    await service.create_playlist(**data,
                                  photo_path = f"https://playlistphotos.s3.eu-north-1.amazonaws.com/{data['title']}_{data['user_id']}.jpg")
    return "Die Wiedergabeliste wurde erfolgreich hinzugefügt"

@router.get("/allMusic", responses = {200: {"model": list[MusicView], "description": "All musics"}})
async def read_all_musics(
        user_id: int,
        service: Annotated[MusicService, Depends(get_music_services)],
        security: Annotated[dict, Depends(oauth2_scheme)]
):
    jwt = await service.get_hwt_operation()
    await jwt.decode_access_token( security )
    return await service.get_all_music(user_id)

@router.get("/allPlaylists", responses = {200: {"model": list[PlaylistView]}})
async def read_playlists(
        user_id: int,
        service: Annotated[MusicService, Depends(get_music_services)],
        security: Annotated[dict, Depends(oauth2_scheme)]
):
    jwt = await service.get_hwt_operation()
    await jwt.decode_access_token(security)
    data = await service.get_all_playlists(user_id=user_id)
    return data

@router.get("/playlist/{id}", responses = {200: {"model": list[PlaylistView]}})
async def read_playlist(
        id: int,
        service: Annotated[MusicService, Depends(get_music_services)],
        security: Annotated[dict, Depends(oauth2_scheme)]
):
    jwt = await service.get_hwt_operation()
    await jwt.decode_access_token(security)
    data = await service.get_playlist_by_id(id)
    loguru.logger.info(data)
    return data

@router.get("/{id}", responses = {200: {"model": MusicView, "description": "Music by id"}})
async def read_music(
        id: int,
        service: Annotated[MusicService, Depends(get_music_services)],
        security: Annotated[dict, Depends(oauth2_scheme)]
):
    return await service.get_music_by_id(id)


@router.delete("/playlist", responses = {200: {"status_message": "Wiedergabeliste entfernt"}})
async def delete_playlist(
        data: dict,

        service: Annotated[MusicService, Depends(get_music_services)],
        security: Annotated[dict, Depends(oauth2_scheme)]
):
    jwt = await service.get_hwt_operation()
    await jwt.decode_access_token(security)
    loguru.logger.info(data)
    await service.delete_file( file_name = data['photo_path'].replace("https://playlistphotos.s3.eu-north-1.amazonaws.com/", "") , bucket_name = "playlistphotos" )
    if len(data['music']) > 0:
        loguru.logger.info("AAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        for music in data['music']:
            await service.delete_file( file_name = music['photo_path'].replace("https://music-photos.s3.eu-north-1.amazonaws.com/", ""), bucket_name = "music-photos")
            await service.delete_file( file_name = music['file_path'].replace("https://musicbasket.s3.eu-north-1.amazonaws.com/", ""), bucket_name = "musicbasket")
    loguru.logger.info(data['id'])
    await service.delete_playlist(id = int(data['id']))
    return {"status_code": 200, "message": "Wiedergabeliste entfernt"}