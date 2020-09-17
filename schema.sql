CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE,
  password TEXT
);


CREATE TABLE restaurants (
  id SERIAL PRIMARY KEY,
  name TEXT,
);

CREATE TABLE schedules (
  id SERIAL PRIMARY KEY,
  restaurantID INT REFERENCES restaurants(id),
  day_of_week INT CHECK (day_of_week IN (1,2,3,4,5,6,7)),
  time_start TIME,
  working_time INT
);
