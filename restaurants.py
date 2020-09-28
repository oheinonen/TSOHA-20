from db import db
from flask import session
from datetime import datetime, timedelta

def add_restaurant(name):
    try:
        sql = "INSERT INTO restaurants (name) VALUES (:name)"
        db.session.execute(sql, {"name":name})
        db.session.commit()
    except:
        return False
    return True

def remove_restaurant(id):
    try:
        sql = "UPDATE restaurants SET visible=0 WHERE id=:id"
        db.session.execute(sql,{"id":id})
        db.session.commit()
    except:
        return False
    return True

def get_name(id):
    sql = "SELECT name FROM restaurants WHERE id=:id AND visible=1"
    result = db.session.execute(sql, {"id":id})
    name = result.fetchone()[0]
    return name

def get_all():
    sql = "SELECT name,id FROM restaurants WHERE visible=1"
    result = db.session.execute(sql)
    restaurants = result.fetchall()
    return restaurants

def get_last_by_name(name):
    sql = "SELECT id  FROM restaurants WHERE name=:name ORDER BY id DESC LIMIT 1"
    result = db.session.execute(sql, {"name":name})
    id = result.fetchone()[0]
    return id
    
# Functions related to shifts in this restaurant

def add_shift(name, restaurantID, role, date, start_time, duration, reps, repetition):
    try:
        date_to_add = date
        for i in range(int(reps)+1):
            if str(repetition) == "daily":
                for j in range(8):
                    sql = "INSERT INTO shifts (name, restaurantID, role, date, start_time, duration) VALUES (:name, :restaurantID, :role, :date, :start_time, :duration)"
                    db.session.execute(sql, {"name":name, "restaurantID":restaurantID, "role":role, "date":date_to_add, "start_time":start_time, "duration":duration})
                    db.session.commit()
                    modified_date = datetime.strptime(date_to_add, "%Y-%m-%d") + timedelta(days=1)
                    date_to_add = modified_date.strftime( "%Y-%m-%d")
            else:
                sql = "INSERT INTO shifts (name, restaurantID, role, date, start_time, duration) VALUES (:name, :restaurantID, :role, :date, :start_time, :duration)"
                db.session.execute(sql, {"name":name, "restaurantID":restaurantID, "role":role, "date":date_to_add, "start_time":start_time, "duration":duration})
                db.session.commit()
                modified_date = datetime.strptime(date_to_add, "%Y-%m-%d") + timedelta(days=7)
                date_to_add = modified_date.strftime( "%Y-%m-%d")
    except:
        return False
    return True

def remove_shift(id):
    try:
        sql = "UPDATE shifts SET visible=0 WHERE id=:id"
        db.session.execute(sql,{"id":id})
        db.session.commit()
    except:
        return False
    return True

def get_shift_name(id):
    sql = "SELECT date FROM shifts WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    name = result.fetchone()[0]
    return name

def get_shift_date(id):
    sql = "SELECT name FROM shifts WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    date = result.fetchone()[0]
    return date

def get_shifts(restaurantID):
    sql = "SELECT name,date, start_time, duration,id FROM shifts WHERE restaurantID=:restaurantID AND visible=1"
    result = db.session.execute(sql, {"restaurantID":restaurantID})
    shifts = result.fetchall()
    return shifts

def get_shifts_by_date(restaurantID,date): 
    sql = "SELECT name, role, start_time, duration,id FROM shifts WHERE date=:date AND restaurantID=:restaurantID AND visible=1"
    result = db.session.execute(sql, {"date":date, "restaurantID":restaurantID})
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

def remove_employee(id):
    try:
        sql = "UPDATE employees SET visible=0 WHERE id=:id"
        db.session.execute(sql,{"id":id})
        db.session.commit()
    except:
        return False
    return True


def get_employee_firstname(id):
    sql = "SELECT firstname FROM employees WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    firstname = result.fetchone()[0]
    return firstname

def get_employee_lastname(id):
    sql = "SELECT lastname FROM employees WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    lastname = result.fetchone()[0]
    return lastname

def get_employees(id):
    sql = "SELECT firstname,lastname,id FROM employees WHERE restaurantID=:id AND visible=1"
    result = db.session.execute(sql, {"id":id})
    employees = result.fetchall()
    return employees

