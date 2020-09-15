CREATE TABLE users (
  id SERIAL PRIMARY KEY;
  username TEXT UNIQUE;
  password TEXT
);

CREATE DOMAIN RoleDomain TEXT
  CHECK (VALUE IN ('leipuri', 'kokki', 'kassahenkilö', 'tarjoilija', ' tiskari' ));

CREATE TABLE roles (
  id SERIAL PRIMARY KEY;
  role RoleDomain;
  restaurantID REFERENCES restaurants(id);
  employeeID REFERENCES employee(id);
)

CREATE TABLE employees (
  id SERIAL PRIMARY KEY;
  name TEXT;
  max_hours INT
)

CREATE TABLE restaurants (
  id SERIAL PRIMARY KEY;
  name TEXT;
  roles RoleDomain
);
