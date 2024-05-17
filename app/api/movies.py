from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import MovieOut, MovieIn
from app.api import db_manager

movies = APIRouter()

@movies.post('/', response_model=MovieOut, status_code=201)
async def create_movie(payload: MovieIn):
    movie_id = await db_manager.add_movie(payload)

    response = {
        'id': movie_id,
        **payload.dict()
    }

    return response


@movies.get('/', response_model=List[MovieOut])
async def get_movies():
    return await db_manager.get_all_movie()


@movies.get('/{id}/', response_model=MovieOut)
async def get_movie(id: int):
    company = await db_manager.get_movie(id)
    if not company:
        raise HTTPException(status_code=404, detail="Movie not found")
    return company


@movies.delete('/{id}/', response_model=None)
async def delete_movie(id: int):
    company = await db_manager.get_movie(id)
    if not company:
        raise HTTPException(status_code=404, detail="Movie not found")
    return await db_manager.delete_movie(id)