from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from datetime import datetime
from app.model.author import Author
from app.model.image import Image
class Article(BaseModel):
    ArticleID: UUID
    Slug: str
    Title: str
    ArticleType: str
    CreatedDate: datetime
    EditedDate: datetime
    Author: Author
    Image: Optional[Image]
    Tags: List[str]
    Keywords: List[str]
    Content: str

def format(tuple: tuple) -> Article:
    return Article (
        ArticleID = tuple[0],
        Slug = tuple[1],
        Title = tuple[2],
        ArticleType = tuple[3],
        CreatedDate = tuple[4],
        EditedDate = tuple[5],
        Author = tuple[6],
        Image = tuple[7],
        Tags = tuple[8] or [],
        Keywords = tuple[9] or [],
        Content = tuple[10]
    )
