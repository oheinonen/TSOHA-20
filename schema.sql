CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE,
  password TEXT
);


CREATE TABLE restaurants (
  id SERIAL PRIMARY KEY,
  name TEXT
);

CREATE TABLE shifts (
  id SERIAL PRIMARY KEY,
  name TEXT,
  restaurantID INT REFERENCES restaurants(id),
  role CHAR(20),
  date DATE CHECK(date BETWEEN '2020-01-01' AND '2025-12-31'),
  start_time TIME,
  duration INT CHECK(duration BETWEEN 0 AND 24)
);