from db import db
from flask import session
from datetime import datetime, timedelta
import random
import restaurants

def add_employee(firstname,lastname,restaurantID, role, max_hours):
    try:
        sql = "INSERT INTO employees (firstname,lastname,restaurantID, role, max_hours) \
               VALUES (:firstname,:lastname,:restaurantID, :role, :max_hours)"
        db.session.execute(sql, {"firstname":firstname,"lastname":lastname,"restaurantID":restaurantID,
                                 "role":role, "max_hours":max_hours})
        db.session.commit()
    except:
        return False
    return True

def update_employee(id,firstname,lastname, role, max_hours):
    try:
        sql = "UPDATE employees SET firstname=:firstname, lastname=:lastname, role=:role, max_hours=:max_hours  WHERE id=:id"
        db.session.execute(sql, {"firstname":firstname,"lastname":lastname, "role":role, "max_hours":max_hours,"id":id})
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

def get_employee(id):
    sql = "SELECT id,firstname,lastname,restaurantID,role,max_hours FROM employees WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    employee = result.fetchone()
    return employee

def get_employees_by_role(id,role):
    sql = "SELECT id,firstname,lastname,restaurantID,role,max_hours \
           FROM employees WHERE restaurantID=:id AND visible=1 AND role=:role"
    result = db.session.execute(sql, {"id":id, "role":role})
    employees = result.fetchall()
    return employees

def add_dayoff(employeeID,date,reason):
    try:
        sql = "INSERT INTO dayoffs (employeeID,date,reason) VALUES (:employeeID, :date, :reason)"
        db.session.execute(sql, {"employeeID":employeeID,"date":date,"reason":reason})
        db.session.commit()
    except:
        try:
            sql = "UPDATE dayoffs SET visible=1, reason=:reason WHERE employeeID=:employeeID AND date=:date"
            db.session.execute(sql,{"employeeID":employeeID, "date":date,"reason":reason})
            db.session.commit()
        except:
            return False
        return True
    return True

def remove_dayoff(employeeID,date):
    try:
        sql = "UPDATE dayoffs SET visible=0 WHERE employeeID=:employeeID AND date=:date"
        db.session.execute(sql,{"employeeID":employeeID, "date":date})
        db.session.commit()
    except:
        return False
    return True

def has_dayoff(employeeID,date):
    sql = "SELECT employeeID,date FROM dayoffs WHERE employeeID=:employeeID AND visible=1 AND date=:date"
    result = db.session.execute(sql, {"employeeID":employeeID, "date":date})
    dayoff = result.fetchone()
    return dayoff


def has_shift(employeeID,date):
    sql = "SELECT COUNT(*) FROM shifts WHERE employeeID=:employeeID AND date=:date"
    result = db.session.execute(sql, {"employeeID":employeeID, "date":date})
    shift = result.fetchone()
    return shift 
    
def own_shifts(employeeID,week):
    employee = get_employee(employeeID)
    restaurant = restaurants.get_restaurant(employee[3])
    shifts = restaurants.get_shifts_by_employee_and_week(restaurant[0],employeeID,week)
    date = datetime.strptime(week + '-1', "%G-W%V-%u").strftime( "%Y-%m-%d")
    schedule = [[]]*7
    # For each day this week, add shifts to schedule which will be returned
    for i in range(7):
        schedule[i] = (i,None)
        for shift in shifts:
            if str(shift.date) == date:
                schedule[i] = (i,shift)
        modified_date = datetime.strptime(date, "%Y-%m-%d") + timedelta(days=1)
        date = modified_date.strftime( "%Y-%m-%d")
    return schedule

def work_report(restaurantID,employeeID,week):
    shifts = restaurants.get_shifts_by_employee_and_week(restaurantID,employeeID,week)
    hours = 0
    for shift in shifts:
        hours += shift.duration
    return hours

# Returns employees in this restaurant in a tuple where:
# 1st element: all employees
# 2nd element: all bakers
# 3rd element: all chefs
# 4th element: all waiters
# 5th element: all cashiers
# 6th element: all dishwashers
def get_employees(id):
    sql = "SELECT id,firstname,lastname,restaurantID,role,max_hours FROM employees WHERE restaurantID=:id AND visible=1"
    result = db.session.execute(sql, {"id":id})
    employees = result.fetchall()
    roles = [[]]*5
    i = 0
    for role in ['Leipuri','Kokki','Tarjoilija','Kassahenkilö','Tiskari']:
        roles[i] = get_employees_by_role(id,role)
        i += 1
    return (employees, roles[0], roles[1], roles[2], roles[3], roles[4])
