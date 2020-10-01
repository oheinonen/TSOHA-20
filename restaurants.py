from db import db
from flask import session
from datetime import datetime, timedelta
import random

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

def employee_has_shift(date,employeeID):
    sql = "SELECT * FROM shifts WHERE employeeID=:employeeID AND date=:date"
    result = db.session.execute(sql, {"employeeID":employeeID, "date":date})
    shift = result.fetchone()[0]
    return True if shift else False 

def add_employee_to_shift(shiftID,employeeID):
    try:
        sql = "UPDATE shifts SET employeeID=:employeeID WHERE id=:shiftID"
        db.session.execute( sql, {"employeeID":employeeID, "shiftID":shiftID})
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

def get_shifts_by_employee_and_week(restaurantID,employeeID,week): 
    start_date = datetime.strptime(week + '-1', "%Y-W%W-%w").strftime( "%Y-%m-%d")
    modified_date = datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=7)
    end_date = modified_date.strftime( "%Y-%m-%d")
    sql = "SELECT * FROM shifts WHERE employeeID=:employeeID AND restaurantID=:restaurantID AND visible=1 AND date BETWEEN :start_date AND :end_date"
    result = db.session.execute(sql, {"employeeID":employeeID, "restaurantID":restaurantID, "start_date":start_date, "end_date":end_date})
    shifts = result.fetchall()
    return shifts

def get_shifts_by_date_and_role(restaurantID,date,role): 
    sql = "SELECT * FROM shifts WHERE date=:date AND restaurantID=:restaurantID AND role=:role AND visible=1"
    result = db.session.execute(sql, {"date":date, "restaurantID":restaurantID, "role":role})
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


# Functions below return list where
# employee[0] = id
# employee[1] = firstname
# employee[2] = lastname
# employee[3] = restaurantID
# employee[4] = role
# employee[5] = max_hours
def get_employee(id):
    sql = "SELECT * FROM employees WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    employee = result.fetchone()
    return employee

def get_employees_by_role(id,role):
    sql = "SELECT * FROM employees WHERE restaurantID=:id AND visible=1 AND role=:role"
    result = db.session.execute(sql, {"id":id, "role":role})
    employees = result.fetchall()
    return employees

# Returns employees in this restaurant in a tuple where:
# 1st element: all employees
# 2nd element: all bakers
# 3rd element: all chefs
# 4th element: all waiters
# 5th element: all cashiers
# 6th element: all dishwashers
def get_employees(id):
    sql = "SELECT * FROM employees WHERE restaurantID=:id AND visible=1"
    result = db.session.execute(sql, {"id":id})
    employees = result.fetchall()
    bakers = get_employees_by_role(id,'Leipuri')
    chefs = get_employees_by_role(id,'Kokki')
    waiters = get_employees_by_role(id,'Tarjoilija')
    cashiers = get_employees_by_role(id,'Kassahenkilö')
    dishwashers = get_employees_by_role(id,'Tiskari')
    return (employees, bakers, chefs, waiters, cashiers, dishwashers)


# Functions related to making staff strength calendar and the roster

# returns list where ith element is list of needed staff for each role in the ith day of the week. the roles are in order
# 1. bakers, 2. chefs, 3. waiters, 4. cashiers, 5. dishwashers
# therefore calendar[1][3] shows how many cashiers are needed on Tuesday
def create_staff_strength_calendar(week,restaurantID):
    calendar = [[]]*7
    date = datetime.strptime(week + '-1', "%G-W%V-%u").strftime( "%Y-%m-%d")
    
    for i in range(7):
        bakers =        len(get_shifts_by_date_and_role(restaurantID,date,'Leipuri'))
        chefs =         len(get_shifts_by_date_and_role(restaurantID,date,'Kokki'))
        waiters =       len(get_shifts_by_date_and_role(restaurantID,date,'Tarjoilija'))
        cashiers =      len(get_shifts_by_date_and_role(restaurantID,date,'Kassahenkilö'))
        dishwashers =   len(get_shifts_by_date_and_role(restaurantID,date,'Tiskari'))
        calendar[i] = [bakers, chefs, waiters, cashiers, dishwashers]
        modified_date = datetime.strptime(date, "%Y-%m-%d") + timedelta(days=1)
        date = modified_date.strftime( "%Y-%m-%d")
    
    return calendar
     
# returns a list where ith element is list of shifts on ith day of the week. The shifts are assigned to employees.
def create_roster(week,restaurantID):
    date = datetime.strptime(week + '-1', "%G-W%V-%u").strftime( "%Y-%m-%d")
    roster = [[]]*7
    for i in range(7):
        shifts = get_shifts_by_date(restaurantID,date)
        this_day_shifts = []
        for shift in shifts:

             # employees are shuffled to create randomness in picking employee
            employees = get_employees_by_role(restaurantID,shift.role)
            employees = random.sample(employees, len(employees))
            for employee in employees:
                has_shift = False
                current_shifts = get_shifts_by_employee_and_week(employee.id,restaurantID,week)
                hours = 0
                for current_shift in current_shifts:
                    # Check if employee already has shift this day
                    if employee_has_shift(employee.id, current_shift.date):
                        has_shift = True
                    else:
                        hours += int(current_shift.duration)
                        print(hours)

                if hours + shift.duration <= employee.max_hours and not has_shift:
                    if add_employee_to_shift(shift.id,employee.id):
                        this_day_shifts.append((shift,employee))
                        break

        roster[i] = this_day_shifts
        modified_date = datetime.strptime(date, "%Y-%m-%d") + timedelta(days=1)
        date = modified_date.strftime( "%Y-%m-%d")
    
    return roster
     