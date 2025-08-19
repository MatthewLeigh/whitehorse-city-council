
from pydantic import BaseModel
from uuid import UUID

class Image(BaseModel):
    ImageID: UUID
    Title: str
    FileName: str

def format(tuple: tuple) -> Image:
    return Image (
        ImageID = tuple[0],
        Title = tuple[1],
        FileName = tuple[2]
    )
