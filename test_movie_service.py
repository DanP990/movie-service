import pytest
from app.api.models import MovieIn, MovieOut

movies = MovieIn(
    name='The Wolf of Wall Street',
    age=10,
    price=10000000,
    county='USA',
)


def test_create_client(movies: MovieIn = movies):
    assert dict(movies) == {'name': movies.name,
                              'age': movies.age,
                              'price': movies.price,
                              'county': movies.county
                              }


def test_update_client_age(movies: MovieIn = movies):
    movies_upd = MovieOut(
        name='The Wolf of Wall Street',
        age=10,
        price=10000000,
        county='USA',
        id=1
    )
    assert dict(movies_upd) == {'name': movies.name,
                              'age': movies.age,
                              'price': movies.price,
                              'county': movies.county,
                              'id': movies_upd.id
                              }


def test_update_client_genre(movies: MovieIn = movies):
    movies_upd = MovieOut(
        name='The Wolf of Wall Street',
        age=10,
        price=10000000,
        county='USA',
        id=1
    )
    assert dict(movies_upd) == {'name': movies.name,
                              'age': movies.age,
                              'price': movies.price,
                              'county': movies.county,
                              'id': movies_upd.id
                              }
