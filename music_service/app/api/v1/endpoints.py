from typing import Annotated

import loguru
from app.schemas.pydantic_schemas import MusicAdd , MusicView, PlaylistAdd, PlaylistView

from fastapi import APIRouter , Depends , UploadFile , File , Form
from fastapi.security import OAuth2PasswordBearer


from app.services.music_service import MusicService
from app.api.v1.dependencies import get_music_services
from app.utils.aws import AWS

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "")

@router.post("/create")
async def create_music(
        service: Annotated[MusicService, Depends(get_music_services)],
        file: Annotated[UploadFile, File(media_type = "audio/mpeg")],
        photo: Annotated[UploadFile, File(media_type = "image/jpeg")],
        items: Annotated[MusicAdd, Depends()]
        ):
    data = items.model_dump()
    loguru.logger.info(data)
    await service.add_data_to_buckets(file = file, data = data, bucket_name = "musicbasket")
    await service.add_data_to_buckets(file = photo, data = data, bucket_name = "music-photos")
    await service.create_music( **data ,
                                file_path = f"https://musicbasket.s3.eu-north-1.amazonaws.com/{data['title']}.mp3" ,
                                photo_path = f"https://music-photos.s3.eu-north-1.amazonaws.com/{data['title']}.jpg" )
    return {"items": items}

@router.post("/playlist", responses = {200: {"model": PlaylistAdd}})
async def create_playlist(items: PlaylistAdd, service: Annotated[MusicService, Depends(get_music_services)]):
    data = items.model_dump()
    await service.create_playlist(**data)
    return {"items": items}

@router.get("/allMusic", responses = {200: {"model": list[MusicView], "description": "All musics"}})
async def read_all_musics(service: Annotated[MusicService, Depends(get_music_services)]):
    return await service.get_all_music()

@router.get("/allPlaylists", responses = {200: {"model": list[PlaylistView]}})
async def read_playlists(service: Annotated[MusicService, Depends(get_music_services)]):
    data = await service.get_all_playlists()
    return data

@router.get("/{id}", responses = {200: {"model": MusicView, "description": "Music by id"}})
async def read_music(id: int, service: Annotated[MusicService, Depends(get_music_services)]):
    return await service.get_music_by_id(id)