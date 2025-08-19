CREATE TABLE Author (
    AuthorID UUID,
    ImageID UUID,
    Prefix TEXT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Suffix TEXT,
    PRIMARY KEY (AuthorID),
    FOREIGN KEY (ImageID) REFERENCES Image(ImageID) ON DELETE CASCADE
);
