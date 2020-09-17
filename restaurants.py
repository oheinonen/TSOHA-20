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

def add_schedule(day_of_week,time_start, working_time, restaurantID):
    try:
        sql = "INSERT INTO schedules (day_of_week,time_start, working_time, restaurantID) VALUES (:day_of_week,:time_start, :working_time, :restaurantID)"
        db.session.execute(sql, {"day_of_week":day_of_week, "time_start":time_start, "working_time":working_time, "restaurantID":restaurantID})
        db.session.commit()
    except:
        return False
    return True

def add_urgency_class(bakers,chefs,waiters, cashiers, dishwashers, restaurantID):
    try:
        sql = "INSERT INTO urgencyClasses (bakers,chefs,waiters, cashiers, dishwashers, restaurantID) VALUES (:bakers,:chefs,:waiters, :cashiers, :dishwashers, :restaurantID)"
        db.session.execute(sql, {"bakers":bakers,"chefs":chefs,"waiters":waiters, "cashiers":cashiers, "dishwashers":dishwashers, "restaurantID": restaurantID})
        db.session.commit()
    except:
        return False

    return True
