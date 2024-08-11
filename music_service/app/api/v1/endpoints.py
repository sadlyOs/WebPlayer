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

@router.post("/playlist", responses = {200: {"model": PlaylistAdd}})
async def create_playlist(
        service: Annotated[MusicService, Depends(get_music_services)],
        security: Annotated[dict, Depends(oauth2_scheme)],
        photo: Annotated[UploadFile, File(media_type="image/jpeg")],
        items: Annotated[PlaylistAdd, Depends()]
):
    jwt = await service.get_hwt_operation()
    await jwt.decode_access_token( security )
    data = items.model_dump()
    loguru.logger.info(data)
    await service.add_data_to_buckets( file = photo , data = data , bucket_name = "playlistphotos" )
    await service.create_playlist(**data,
                                  photo_path = f"https://playlistphotos.s3.eu-north-1.amazonaws.com/{data['title']}.jpg")
    return {"items": items}

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

@router.get("/playlist/{id}")
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

