CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(30) UNIQUE ,
  password TEXT
);


CREATE TABLE restaurants (
  id SERIAL PRIMARY KEY,
  owner INT REFERENCES users(id),
  name VARCHAR(50) UNIQUE,
  visible INT DEFAULT 1 CHECK(visible IN (0,1))
);

CREATE TABLE employees (
  id SERIAL PRIMARY KEY,
  firstname VARCHAR(50),
  lastname VARCHAR(50),
  restaurantID INT REFERENCES restaurants(id),
  role VARCHAR(20),
  max_hours INT CHECK(max_hours BETWEEN 0 AND 100),
  visible INT DEFAULT 1 CHECK(visible IN (0,1))
);

CREATE TABLE shifts (
  id SERIAL PRIMARY KEY,
  name TEXT,
  restaurantID INT REFERENCES restaurants(id),
  employeeID INT REFERENCES employees(id),
  role VARCHAR(20),
  date DATE CHECK(date BETWEEN '2020-01-01' AND '2025-12-31'),
  start_time TIME,
  duration INT CHECK(duration BETWEEN 0 AND 24),
  visible INT DEFAULT 1 CHECK(visible IN (0,1))
);

CREATE TABLE dayoffs (
  id SERIAL PRIMARY KEY,
  employeeID INT REFERENCES employees(id),
  date DATE CHECK(date BETWEEN '2020-01-01' AND '2025-12-31'),
  reason TEXT,
  visible INT DEFAULT 1 CHECK(visible IN (0,1))
);

INSERT INTO restaurants (owner,name) VALUES (1,'Ravintola 1');INSERT INTO restaurants (owner,name) VALUES (1,'Ravintola 2');INSERT INTO restaurants (owner,name) VALUES (1,'Ravintola 3');INSERT INTO restaurants (owner,name) VALUES (1,'Ravintola 4');INSERT INTO restaurants (owner,name) VALUES (1,'Ravintola 5');
INSERT INTO restaurants (owner,name) VALUES (2,'Ravintola 11');INSERT INTO restaurants (owner,name) VALUES (2,'Ravintola 22');INSERT INTO restaurants (owner,name) VALUES (2,'Ravintola 33');INSERT INTO restaurants (owner,name) VALUES (2,'Ravintola 44');INSERT INTO restaurants (owner,name) VALUES (2,'Ravintola 55');
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu1','suku1',3,'Leipuri',10);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu2','suku2',3,'Leipuri',20);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu3','suku3',3,'Leipuri',30);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu4','suku4',3,'Leipuri',40);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu5','suku5',3,'Leipuri',50);

INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu6','suku6',3,'Kokki',10);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu7','suku7',3,'Kokki',20);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu8','suku8',3,'Kokki',30);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu9','suku9',3,'Kokki',40);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu10','suku10',3,'Kokki',50);

INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu11','suku11',3,'Tarjoilija',10);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu12','suku12',3,'Tarjoilija',20);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu13','suku13',3,'Tarjoilija',30);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu14','suku14',3,'Tarjoilija',40);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu15','suku15',3,'Tarjoilija',50);

INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu16','suku16',3,'Kassahenkilö',10);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu17','suku17',3,'Kassahenkilö',20);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu18','suku18',3,'Kassahenkilö',30);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu19','suku19',3,'Kassahenkilö',40);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu20','suku20',3,'Kassahenkilö',50);

INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu21','suku21',3,'Tiskari',10);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu22','suku22',3,'Tiskari',20);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu23','suku23',3,'Tiskari',30);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu24','suku24',3,'Tiskari',40);
INSERT INTO employees (firstname,lastname,restaurantID,role,max_hours) VALUES ('etu25','suku25',3,'Tiskari',50);

INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamutiski',3,'Tiskari', '2020-10-18', '06:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamutiski',3,'Tiskari', '2020-10-19', '06:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamutiski',3,'Tiskari', '2020-10-20', '06:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamutiski',3,'Tiskari', '2020-10-21', '06:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamutiski',3,'Tiskari', '2020-10-22', '06:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamutiski',3,'Tiskari', '2020-10-23', '06:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamutiski',3,'Tiskari', '2020-10-24', '06:00:00',8);

INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltatiski',3,'Tiskari', '2020-10-18', '14:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltatiski',3,'Tiskari', '2020-10-19', '14:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltatiski',3,'Tiskari', '2020-10-20', '14:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltatiski',3,'Tiskari', '2020-10-21', '14:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltatiski',3,'Tiskari', '2020-10-22', '14:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltatiski',3,'Tiskari', '2020-10-23', '14:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltatiski',3,'Tiskari', '2020-10-24', '14:00:00',8);

INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamukokki',3,'Kokki', '2020-10-18', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamukokki',3,'Kokki', '2020-10-19', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamukokki',3,'Kokki', '2020-10-20', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamukokki',3,'Kokki', '2020-10-21', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamukokki',3,'Kokki', '2020-10-22', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamukokki',3,'Kokki', '2020-10-23', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamukokki',3,'Kokki', '2020-10-24', '10:00:00',10);

INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltakokki',3,'Kokki', '2020-10-18', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltakokki',3,'Kokki', '2020-10-19', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltakokki',3,'Kokki', '2020-10-20', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltakokki',3,'Kokki', '2020-10-21', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltakokki',3,'Kokki', '2020-10-22', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltakokki',3,'Kokki', '2020-10-23', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltakokki',3,'Kokki', '2020-10-24', '15:00:00',10);

INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamutarjoilija',3,'Tarjoilija', '2020-10-18', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamutarjoilija',3,'Tarjoilija', '2020-10-19', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamutarjoilija',3,'Tarjoilija', '2020-10-20', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamutarjoilija',3,'Tarjoilija', '2020-10-21', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamutarjoilija',3,'Tarjoilija', '2020-10-22', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamutarjoilija',3,'Tarjoilija', '2020-10-23', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamutarjoilija',3,'Tarjoilija', '2020-10-24', '10:00:00',10);

INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltatarjoilija',3,'Tarjoilija', '2020-10-18', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltatarjoilija',3,'Tarjoilija', '2020-10-19', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltatarjoilija',3,'Tarjoilija', '2020-10-20', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltatarjoilija',3,'Tarjoilija', '2020-10-21', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltatarjoilija',3,'Tarjoilija', '2020-10-22', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltatarjoilija',3,'Tarjoilija', '2020-10-23', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltatarjoilija',3,'Tarjoilija', '2020-10-24', '15:00:00',10);

INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamukassa',3,'Kassahenkilö', '2020-10-18', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamukassa',3,'Kassahenkilö', '2020-10-19', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamukassa',3,'Kassahenkilö', '2020-10-20', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamukassa',3,'Kassahenkilö', '2020-10-21', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamukassa',3,'Kassahenkilö', '2020-10-22', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamukassa',3,'Kassahenkilö', '2020-10-23', '10:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamukassa',3,'Kassahenkilö', '2020-10-24', '10:00:00',10);

INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltakassa',3,'Kassahenkilö', '2020-10-18', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltakassa',3,'Kassahenkilö', '2020-10-19', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltakassa',3,'Kassahenkilö', '2020-10-20', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltakassa',3,'Kassahenkilö', '2020-10-21', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltakassa',3,'Kassahenkilö', '2020-10-22', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltakassa',3,'Kassahenkilö', '2020-10-23', '15:00:00',10);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltakassa',3,'Kassahenkilö', '2020-10-24', '15:00:00',10);

INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamupulla',3,'Leipuri', '2020-10-18', '06:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamupulla',3,'Leipuri', '2020-10-19', '06:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamupulla',3,'Leipuri', '2020-10-20', '06:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamupulla',3,'Leipuri', '2020-10-21', '06:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamupulla',3,'Leipuri', '2020-10-22', '06:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamupulla',3,'Leipuri', '2020-10-23', '06:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('aamupulla',3,'Leipuri', '2020-10-24', '06:00:00',8);

INSERT INTO shifts (name,restauranrtID,role,date,start_time,duration) VALUES ('iltapulla',3,'Leipuri', '2020-10-18', '14:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltapulla',3,'Leipuri', '2020-10-19', '14:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltapulla',3,'Leipuri', '2020-10-20', '14:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltapulla',3,'Leipuri', '2020-10-21', '14:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltapulla',3,'Leipuri', '2020-10-22', '14:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltapulla',3,'Leipuri', '2020-10-23', '14:00:00',8);
INSERT INTO shifts (name,restaurantID,role,date,start_time,duration) VALUES ('iltapulla',3,'Leipuri', '2020-10-24', '14:00:00',8);
