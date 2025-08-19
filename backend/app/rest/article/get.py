from app.query.fetch_one import execute
from app.model.article import Article, format
from fastapi import HTTPException

def get(article_slug: str) -> Article:
    response = execute(query(), value(article_slug))
    if response is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return format(response)

def query():
    return """
        SELECT 
            Article.ArticleID,
            Article.Slug,
            Article.Title,
            Article.ArticleType,
            Article.CreatedDate,
            Article.EditedDate,

            (
                SELECT json_build_object(
                    'AuthorID', AuthorID,
                    'Prefix', Prefix,
                    'FirstName', FirstName,
                    'LastName', LastName,
                    'Suffix', Suffix,
                    'Image', (
                        SELECT json_build_object(
                            'ImageID', ImageID,
                            'Title', Title,
                            'FileName', FileName
                        )
                        FROM Image
                        WHERE Image.ImageID = Author.ImageID
                    )
                )
                FROM Author
                WHERE Author.AuthorID = Article.AuthorID
            ) AS Author,
            
            (
                SELECT json_build_object(
                    'ImageID', ImageID,
                    'Title', Title,
                    'FileName', FileName
                )
                FROM Image
                WHERE Image.ImageID = Article.ImageID
            ) AS Image,

            (
                SELECT json_agg(Tag)
                FROM Tag
                WHERE Tag.ArticleID = Article.ArticleID
            ) AS Tags,

            (
                SELECT json_agg(Keyword)
                FROM Keyword
                WHERE Keyword.ArticleID = Article.ArticleID
            ) AS Keywords,

            Article.Content

        FROM Article
        WHERE Article.Slug = %s;
    """

def value(article_slug: str):
    return (str(article_slug),)