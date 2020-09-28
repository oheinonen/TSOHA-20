from db import db
from flask import session

def add_restaurant(name):
    try:
        sql = "INSERT INTO restaurants (name) VALUES (:name)"
        db.session.execute(sql, {"name":name})
        db.session.commit()
    except:
        return False
    return True

def get_name(id):
    sql = "SELECT name FROM restaurants WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    name = result.fetchone()[0]
    return name

def get_all():
    sql = "SELECT name,id FROM restaurants"
    result = db.session.execute(sql)
    restaurants = result.fetchall()
    return restaurants

def get_last_by_name(name):
    sql = "SELECT id  FROM restaurants WHERE name=:name ORDER BY id DESC LIMIT 1"
    result = db.session.execute(sql, {"name":name})
    id = result.fetchone()[0]
    return id
# Functions related to shifts in this restaurant

def add_shift(name, restaurantID, role, date, start_time, duration):
    try:
        sql = "INSERT INTO shifts (name, restaurantID, role, date, start_time, duration) VALUES (:name, :restaurantID, :role, :date, :start_time, :duration)"
        db.session.execute(sql, {"name":name, "restaurantID":restaurantID, "role":role, "date":date, "start_time":start_time, "duration":duration})
        db.session.commit()
    except:
        return False
    return True

def get_shifts(id):
    sql = "SELECT name,date, start_time, duration FROM shifts WHERE restaurantID=" + str(id)
    result = db.session.execute(sql)
    shifts = result.fetchall()
    return shifts

def get_shifts_by_date(id,date): 
    sql = "SELECT name, role, start_time, duration FROM shifts WHERE date='" + str(date) + "' AND restaurantID=" + str(id)
    result = db.session.execute(sql)
    shifts = result.fetchall()
    return shifts

# Functions related to employees in this restaurant

def add_employee(firstname,lastname,restaurantID, role, max_hours):
    try:
        sql = "INSERT INTO employees (firstname,lastname,restaurantID, role, max_hours) VALUES (:firstname,:lastname,:restaurantID, :role, :max_hours)"
        db.session.execute(sql, {"firstname":firstname,"lastname":lastname,"restaurantID":restaurantID, "role":role, "max_hours":max_hours})
        db.session.commit()
    except:
        return False
    return True

def get_employees(id):
    sql = "SELECT firstname,lastname FROM employees WHERE restaurantID=" + str(id)
    result = db.session.execute(sql)
    employees = result.fetchall()
    return employees

