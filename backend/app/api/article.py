from fastapi import APIRouter, Query, status, Body
from typing import Optional
from app.model.article import Article
from app.model.article_brief import ArticleBrief
from app.rest.article.get import get
from app.rest.article.get_all import get_all

article = APIRouter()

# GET
@article.get("/{article_slug}", response_model=Article)
def get_(article_slug: str):
    return get(article_slug)

# GET Brief | Filterable
@article.get("/", response_model=list[ArticleBrief])
def get_all_(
    title: Optional[str] = None,
    article_type: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[list[str]] = Query(default=None),
    keywords: Optional[list[str]] = Query(default=None),
):
    return get_all(title, article_type, author, tags, keywords)