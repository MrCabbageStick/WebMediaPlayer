DROP TABLE IF EXISTS genre_per_movie;
DROP TABLE IF EXISTS my_lists;
DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    display_name TEXT NOT NULL,
    password TEXT NOT NULL,
    added_on TEXT
);

CREATE TABLE IF NOT EXISTS genres(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    path TEXT NOT NULL,
    thumbnail_path TEXT,
    duration INTEGER
);

CREATE TABLE IF NOT EXISTS genre_per_movie(
    movie_id INTEGER,
    genre_id INTEGER,
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    FOREIGN KEY (genre_id) REFERENCES genres(id),
    PRIMARY KEY (movie_id, genre_id)
);

CREATE TABLE IF NOT EXISTS my_lists(
    user_id INTEGER,
    movie_id INTEGER,
    added_on TEXT NOT NULL,
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    PRIMARY KEY (movie_id, user_id)
);