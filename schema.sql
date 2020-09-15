CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT UNIQUE,
  password TEXT
);

CREATE DOMAIN RoleDomain TEXT
  CHECK (VALUE IN ('leipuri', 'kokki', 'kassahenkilö', 'tarjoilija', ' tiskari' ));

CREATE TABLE workrelationships (
  id SERIAL PRIMARY KEY,
  role RoleDomain,
  restaurantID REFERENCES restaurants(id) ON DELETE CASCADE,
  employeeID REFERENCES employee(id) ON DELETE CASCADE
);

CREATE TABLE employees (
  id SERIAL PRIMARY KEY,
  restaurantID REFERENCES restaurants(id) ON DELETE CASCADE,
  name TEXT,
  max_hours INT
);

CREATE TABLE restaurants (
  id SERIAL PRIMARY KEY,
  name TEXT
);
