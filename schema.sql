CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    password TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE
);

CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    author_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_on TEXT DEFAULT (datetime('now')),
    slug TEXT NOT NULL UNIQUE,
    status INTEGER DEFAULT 0,
    title TEXT NOT NULL,
    updated_on TEXT DEFAULT (datetime('now')),
    FOREIGN KEY(author_id) REFERENCES users(id)
);

INSERT INTO
    users(email, first_name, last_name, password, username)
VALUES
    ('test@admin.com', 'Test', 'Admin', 'pass', 'admin');
