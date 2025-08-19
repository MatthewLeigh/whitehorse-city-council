CREATE TABLE Keyword (
    ArticleID UUID,
    Keyword TEXT,
    PRIMARY KEY (ArticleID, Keyword),
    FOREIGN KEY (ArticleID) REFERENCES Article(ArticleID) ON DELETE CASCADE
);
