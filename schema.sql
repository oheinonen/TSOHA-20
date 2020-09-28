CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE,
  password TEXT
);


CREATE TABLE restaurants (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE,
  visible INT DEFAULT 1 CHECK(visible IN (0,1))
);

CREATE TABLE shifts (
  id SERIAL PRIMARY KEY,
  name TEXT,
  restaurantID INT REFERENCES restaurants(id),
  employeeID INT REFERENCES employees(id),
  role CHAR(20),
  date DATE CHECK(date BETWEEN '2020-01-01' AND '2025-12-31'),
  start_time TIME,
  duration INT CHECK(duration BETWEEN 0 AND 24),
  visible INT DEFAULT 1 CHECK(visible IN (0,1))
);

CREATE TABLE employees (
  id SERIAL PRIMARY KEY,
  firstname TEXT,
  lastname TEXT,
  restaurantID INT REFERENCES restaurants(id),
  role CHAR(20),
  max_hours INT CHECK(max_hours BETWEEN 0 AND 100),
  visible INT DEFAULT 1 CHECK(visible IN (0,1))
);
