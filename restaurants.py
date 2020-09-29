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

def update_restaurant(id,name):
    try:
        sql = "UPDATE restaurants SET name=:name WHERE id=:id"
        db.session.execute(sql,{"id":id, "name":name})
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

def update_shift(id, name, role, date, start_time, duration):
    try:
        sql = "UPDATE shifts SET name=:name, role=:role, date=:date, start_time=:start_time, duration=:duration WHERE id=:id"
        db.session.execute(sql, {"name":name, "role":role, "date":date, "start_time":start_time, "duration":duration, "id":id})
        db.session.commit()
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

# Functions below return list where
# shift[0] = id
# shift[1] = name
# shift[2] = restaurantID
# shift[3] = role
# shift[4] = date
# shift[5] = start_time
# shift[6] = duration
# shift[7] = employeeID
def get_shift(id):
    sql = "SELECT * FROM shifts WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    shift = result.fetchone()
    return shift

def get_shifts(restaurantID):
    sql = "SELECT * FROM shifts WHERE restaurantID=:restaurantID AND visible=1"
    result = db.session.execute(sql, {"restaurantID":restaurantID})
    shifts = result.fetchall()
    return shifts

def get_shifts_by_date(restaurantID,date): 
    sql = "SELECT * FROM shifts WHERE date=:date AND restaurantID=:restaurantID AND visible=1"
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

def update_employee(id,firstname,lastname, role, max_hours):
    try:
        sql = "UPDATE employees SET(firstname=:firstname,lastname=:lastname, role=:role, max_hours=:max_hours) WHERE id=:id"
        db.session.execute(sql, {"firstname":firstname,"lastname":lastname, "role":role, "max_hours":max_hours})
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


# Returns list where
# employee[0] = id
# employee[1] = first name
# employee[2] = last name
# employee[3] = restaurantID
# employee[4] = role
# employee[5] = max_hours
def get_employee(id):
    sql = "SELECT * FROM employees WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    employee = result.fetchone()
    return employee


# Returns employees in this restaurant in a tuple where:
# 1st element: all employees
# 2nd element: all bakers
# 3rd element: all chefs
# 4th element: all waiters
# 5th element: all cashiers
# 6th element: all dishwashers
def get_employees(id):
    # All employees
    sql = "SELECT * FROM employees WHERE restaurantID=:id AND visible=1"
    result = db.session.execute(sql, {"id":id})
    employees = result.fetchall()
    # bakers
    sql = "SELECT * FROM employees WHERE restaurantID=:id AND visible=1 AND role='Leipuri'"
    result = db.session.execute(sql, {"id":id})
    bakers = result.fetchall()
    # chefs
    sql = "SELECT * FROM employees WHERE restaurantID=:id AND visible=1 AND role='Kokki'"
    result = db.session.execute(sql, {"id":id})
    chefs = result.fetchall()
    # waiters
    sql = "SELECT * FROM employees WHERE restaurantID=:id AND visible=1 AND role='Tarjoilija'"
    result = db.session.execute(sql, {"id":id})
    waiters = result.fetchall()
    # cashiers
    sql = "SELECT * FROM employees WHERE restaurantID=:id AND visible=1 AND role='Kassahenkilö'"
    result = db.session.execute(sql, {"id":id})
    cashiers = result.fetchall()
    # dishwashers
    sql = "SELECT * FROM employees WHERE restaurantID=:id AND visible=1 AND role='Tiskari'"
    result = db.session.execute(sql, {"id":id})
    dishwashers = result.fetchall()
    return (employees, bakers, chefs, waiters, cashiers, dishwashers)

