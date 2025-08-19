CREATE TABLE Tag (
    ArticleID UUID,
    Tag ARTICLE_TAG,
    PRIMARY KEY (ArticleID, Tag),
    FOREIGN KEY (ArticleID) REFERENCES Article(ArticleID) ON DELETE CASCADE
);
