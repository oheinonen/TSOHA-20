from db import db
from flask import session
from datetime import datetime, timedelta
import random
import employees

def add_restaurant(name,owner):
    try:
        sql = "INSERT INTO restaurants (name,owner) VALUES (:name, :owner)"
        db.session.execute(sql, {"name":name, "owner":owner})
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

# id, owner, name
def get_restaurant(id):
    sql = "SELECT id,owner,name FROM restaurants WHERE id=:id AND visible=1"
    result = db.session.execute(sql, {"id":id})
    restaurant = result.fetchone()
    return restaurant

def get_all(owner):
    sql = "SELECT id,owner,name FROM restaurants WHERE visible=1 AND owner=:owner"
    result = db.session.execute(sql,{"owner":owner})
    restaurants = result.fetchall()
    return restaurants

def get_last(name):
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
                    sql = "INSERT INTO shifts (name, restaurantID, role, date, start_time, duration) \
                           VALUES (:name, :restaurantID, :role, :date, :start_time, :duration)"
                    db.session.execute(sql, {"name":name, "restaurantID":restaurantID, "role":role,
                                             "date":date_to_add, "start_time":start_time, "duration":duration})
                    db.session.commit()
                    modified_date = datetime.strptime(date_to_add, "%Y-%m-%d") + timedelta(days=1)
                    date_to_add = modified_date.strftime( "%Y-%m-%d")
            else:
                sql = "INSERT INTO shifts (name, restaurantID, role, date, start_time, duration) \
                       VALUES (:name, :restaurantID, :role, :date, :start_time, :duration)"
                db.session.execute(sql, {"name":name, "restaurantID":restaurantID, "role":role, "date":date_to_add, 
                                        "start_time":start_time, "duration":duration})
                db.session.commit()
                modified_date = datetime.strptime(date_to_add, "%Y-%m-%d") + timedelta(days=7)
                date_to_add = modified_date.strftime( "%Y-%m-%d")
    except:
        return False
    return True

def update_shift(id, name, role, date, start_time, duration,keep_employee):
    try:
        sql = "UPDATE shifts SET name=:name, role=:role, date=:date, start_time=:start_time, duration=:duration WHERE id=:id"
        db.session.execute(sql, {"name":name, "role":role, "date":date, "start_time":start_time, "duration":duration, "id":id})
        db.session.commit()
        if str(keep_employee)=="REMOVE":
            sql = "UPDATE shifts SET employeeID=NULL WHERE id=:id"
            db.session.execute(sql,{"id":id})
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


def assign__shift(shiftID,employeeID):
    try:
        sql = "UPDATE shifts SET employeeID=:employeeID WHERE id=:shiftID"
        db.session.execute( sql, {"employeeID":employeeID, "shiftID":shiftID})
        db.session.commit()
    except:
        return False
    return True

def get_shift(id):
    sql = "SELECT id,name,restaurantID,employeeID,role,date,start_time,duration FROM shifts WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    shift = result.fetchone()
    return shift

def get_shifts(restaurantID):
    sql = "SELECT id,name,restaurantID,employeeID,role,date,start_time,duration \
           FROM shifts WHERE restaurantID=:restaurantID AND visible=1"
    result = db.session.execute(sql, {"restaurantID":restaurantID})
    shifts = result.fetchall()
    return shifts

def get_shifts_by_date(restaurantID,date): 
    sql = "SELECT id,name,restaurantID,employeeID,role,date,start_time,duration \
           FROM shifts WHERE date=:date AND restaurantID=:restaurantID AND visible=1"
    result = db.session.execute(sql, {"date":date, "restaurantID":restaurantID})
    shifts = result.fetchall()
    return shifts

def get_shifts_by_employee_and_week(restaurantID,employeeID,week): 
    start_date = datetime.strptime(week + '-1', "%G-W%V-%u").strftime( "%Y-%m-%d")
    modified_date = datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=7)
    end_date = modified_date.strftime( "%Y-%m-%d")
    sql = "SELECT id,name,restaurantID,employeeID,role,date,start_time,duration FROM shifts \
           WHERE employeeID=:employeeID AND restaurantID=:restaurantID AND visible=1 AND date BETWEEN :start_date AND :end_date"
    result = db.session.execute(sql, {"employeeID":employeeID, "restaurantID":restaurantID, "start_date":start_date, "end_date":end_date})
    shifts = result.fetchall()
    return shifts

def get_shifts_by_date_and_role(restaurantID,date,role): 
    sql = "SELECT id,name,restaurantID,employeeID,role,date,start_time,duration \
           FROM shifts WHERE date=:date AND restaurantID=:restaurantID AND role=:role AND visible=1"
    result = db.session.execute(sql, {"date":date, "restaurantID":restaurantID, "role":role})
    shifts = result.fetchall()
    return shifts

def is_assigned(id):
    sql = "SELECT employeeID FROM shifts WHERE id=:id"
    result = db.session.execute(sql,{"id":id})
    employeeID = result.fetchone()[0]
    return employeeID

# Functions related to making staff strength calendar and the roster

# returns list where ith element is list of needed staff for each role in the ith day of the week. the roles are in order
# 1. bakers, 2. chefs, 3. waiters, 4. cashiers, 5. dishwashers
# therefore calendar[1][3] shows how many cashiers are needed on Tuesday
def create_staff_strength_calendar(week,restaurantID):
    calendar = [[]]*7
    date = datetime.strptime(week + '-1', "%G-W%V-%u").strftime( "%Y-%m-%d")
    
    for i in range(7):
        roles = [[]]*5
        j = 0
        for role in ['Leipuri','Kokki','Tarjoilija','Kassahenkilö','Tiskari']:
            roles[j] = len(get_shifts_by_date_and_role(restaurantID,date,role))
            j += 1
        calendar[i] = [roles[0], roles[1], roles[2], roles[3], roles[4]]
        modified_date = datetime.strptime(date, "%Y-%m-%d") + timedelta(days=1)
        date = modified_date.strftime( "%Y-%m-%d")
    
    return calendar
     
# returns a list where ith element is list of shifts on ith day of the week. The shifts are assigned to employees.
def create_roster(week,restaurantID):
    date = datetime.strptime(week + '-1', "%G-W%V-%u").strftime( "%Y-%m-%d")
    roster = [[]]*7
    assigned_shifts = []
    not_assigned = []
    assigned_hours = 0
    for i in range(7):
        shifts = get_shifts_by_date(restaurantID,date)
        this_day_shifts = []
        for shift in shifts:
             # employees are shuffled to create randomness in picking employee
            fit_employees = employees.get_employees_by_role(restaurantID,shift.role)
            fit_employees = random.sample(fit_employees, len(fit_employees))
            for employee in fit_employees:
                current_shifts = get_shifts_by_employee_and_week(restaurantID,employee.id,week)
                hours = 0
                for current_shift in current_shifts:
                    hours += int(current_shift.duration)
                able_to_work = not employees.has_shift(employee.id, shift.date) and not employees.has_dayoff(employee.id,shift.date)
                # If employee is already assigned to this shift, information is salvaged so it can be shown to user.
                if is_assigned(shift.id)== employee.id:
                    assigned_hours += shift.duration
                    assigned_to = employees.get_employee(is_assigned(shift.id))                    
                    assigned_shifts.append((shift,assigned_to))
                if hours + shift.duration <= employee.max_hours and able_to_work and not is_assigned(shift.id):
                    # If shift is successfully assigned, move to next shift
                    if assign__shift(shift.id,employee.id):
                        this_day_shifts.append((shift,employee))
                        break 
            # If shift is not successfully assigned, information is salvaged so it can be shown to user.
            if not is_assigned(shift.id):
                not_assigned.append(shift)  

        roster[i] = this_day_shifts
        modified_date = datetime.strptime(date, "%Y-%m-%d") + timedelta(days=1)
        date = modified_date.strftime( "%Y-%m-%d")
    print(roster)
    return (roster,max(unused_hours(week,restaurantID,roster) - assigned_hours,0),assigned_shifts,not_assigned)
     
# counts unused working hours in particular restaurant and week using created roster
def unused_hours(week,restaurantID,roster):
    hours = 0
    all_employees = employees.get_employees(restaurantID)[0]
    date = datetime.strptime(week + '-1', "%G-W%V-%u").strftime( "%Y-%m-%d")
    for employee in all_employees:
        hours += employee[5]
    roster_hours = 0
    for day in roster:
        for (shift,employee) in day:
            roster_hours += shift.duration
    return hours - roster_hours
