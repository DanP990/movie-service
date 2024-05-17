from pydantic import BaseModel
from typing import List, Optional

class MovieIn(BaseModel):
    name: str
    age: int
    price: int
    county: str


class MovieOut(MovieIn):
    id: int
