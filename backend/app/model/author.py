
from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from app.model.image import Image

class Author(BaseModel):
    AuthorID: UUID
    Prefix: Optional[str] = None
    FirstName: str
    LastName: str
    Suffix: Optional[str] = None
    Image: Image

def format(tuple: tuple) -> Author:
    return Author (
        AuthorID = tuple[0],
        Prefix = tuple[1],
        FirstName = tuple[2],
        LastName = tuple[3],
        Suffix = tuple[4],
        Image = tuple[5]
    )
