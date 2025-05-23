
CREATE TABLE IF NOT EXISTS Cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    brand TEXT NOT NULL,
    year INTEGER NOT NULL,
    image_url TEXT
);

CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Ratings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    car_id INTEGER,
    rating INTEGER CHECK(rating >= 1 AND rating <= 5),
    FOREIGN KEY(user_id) REFERENCES Users(id),
    FOREIGN KEY(car_id) REFERENCES Cars(id)
);

CREATE TABLE IF NOT EXISTS Comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    car_id INTEGER,
    comment TEXT,
    FOREIGN KEY(user_id) REFERENCES Users(id),
    FOREIGN KEY(car_id) REFERENCES Cars(id)
);
