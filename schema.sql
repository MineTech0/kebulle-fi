CREATE TABLE regions (
id SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL
);

CREATE TABLE cities (
id SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL,
region_id INTEGER REFERENCES regions(id) ON DELETE CASCADE
);

CREATE TABLE restaurants (
id SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL,
address VARCHAR(255) NOT NULL,
city_id INTEGER REFERENCES cities(id) ON DELETE CASCADE,
rating INTEGER NOT NULL,
created_at DATE NOT NULL,
updated_at DATE NOT NULL
);

CREATE TABLE reviews (
id SERIAL PRIMARY KEY,
user_name VARCHAR(255) NOT NULL,
comment VARCHAR(1000),
date DATE NOT NULL,
sauce_rating INTEGER NOT NULL,
meat_rating INTEGER NOT NULL,
service_rating INTEGER NOT NULL,
price_rating INTEGER NOT NULL,
cleanliness_rating INTEGER NOT NULL,
sides_rating INTEGER NOT NULL,
fries_rating INTEGER NOT NULL,
vegan_options BOOLEAN NOT NULL,
created_at DATE NOT NULL,
restaurant_id INTEGER REFERENCES restaurants(id) ON DELETE CASCADE
);

CREATE TABLE votes (
id SERIAL PRIMARY KEY,
user_name VARCHAR(255) NOT NULL,
vote BOOLEAN NOT NULL,
created_at DATE NOT NULL,
restaurant_id INTEGER REFERENCES restaurants(id) ON DELETE CASCADE
);

INSERT INTO regions (name)
VALUES ('Ahvenanmaa'),
       ('Etelä-Karjala'),
       ('Etelä-Pohjanmaa'),
       ('Etelä-Savo'),
       ('Kainuu'),
       ('Kanta-Häme'),
       ('Keski-Pohjanmaa'),
       ('Keski-Suomi'),
       ('Kymenlaakso'),
       ('Lappi'),
       ('Päijät-Häme'),
       ('Pirkanmaa'),
       ('Pohjanmaa'),
       ('Pohjois-Karjala'),
       ('Pohjois-Pohjanmaa'),
       ('Pohjois-Savo'),
       ('Satakunta'),
       ('Uusimaa'),
       ('Varsinais-Suomi');