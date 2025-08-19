from typing import Optional, List, Tuple
from app.query.fetch_list import execute
from app.model.article_brief import ArticleBrief, format
from app.util.list_to_array_string import list_to_array_string


def get_all(
    title: Optional[str] = None,
    article_type: Optional[str] = None,
    author: Optional[str] = None,
    tags: Optional[str] = None,
    keywords: Optional[str] = None
) -> list[ArticleBrief]:

    query, params = prepare(
        title=title,
        article_type=article_type,
        author_first_name=author,
        author_last_name=author,
        tags=tags,
        keywords=keywords
    )
    rows = execute(query, params)
    return [format(row) for row in rows]


def prepare(
    title: Optional[str] = None,
    article_type: Optional[str] = None,
    author_first_name: Optional[str] = None,
    author_last_name: Optional[str] = None,
    tags: Optional[List[str]] = None,
    keywords: Optional[List[str]] = None,
) -> Tuple[str, list]:

    query = """
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
            ) AS Image

        FROM Article
        JOIN Author ON Author.AuthorID = Article.AuthorID
    """

    filters = []
    params = []

    if title:
        filters.append("Article.Title ILIKE %s")
        params.append(f"%{title}%")

    if article_type:
        filters.append("Article.ArticleType = %s")
        params.append(article_type)

    if author_first_name:
        filters.append("Author.FirstName ILIKE %s")
        params.append(f"%{author_first_name}%")

    if author_last_name:
        filters.append("Author.LastName ILIKE %s")
        params.append(f"%{author_last_name}%")

    if tags:
        filters.append("""
            EXISTS (
                SELECT 1 FROM Tag
                WHERE Tag.ArticleID = Article.ArticleID
                AND Tag.Tag ILIKE ANY(%s::TAG[])
            )
        """)
        params.append(list_to_array_string(tags))

    if keywords:
        filters.append("""
            EXISTS (
                SELECT 1 FROM Keyword
                WHERE Keyword.ArticleID = Article.ArticleID
                AND Keyword.Keyword ILIKE ANY(%s::TAG[])
            )
        """)
        params.append(list_to_array_string(keywords))

    if filters:
        query += " WHERE " + " AND ".join(filters)

    return query, params