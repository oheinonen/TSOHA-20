from app import app
from flask import render_template, request, redirect,session, url_for
from db import db
import users, restaurants

@app.route("/")
def index():
    # List all restaurants currently added to the website
    all_restaurants = restaurants.get_all()
    return render_template("index.html", restaurants=all_restaurants)

@app.route("/restaurant/<int:id>")
def restaurant(id):
    name = restaurants.get_name(id)
    shifts = restaurants.get_shifts(id)
    employees = restaurants.get_employees(id)
    return render_template("restaurant.html", id=id, name=name, shifts=shifts, employees=employees)

@app.route("/restaurant/dayview")
def restaurant_dayview():
    id = request.args["id"]
    date = request.args["date"]
    name = restaurants.get_name(id)
    shifts = restaurants.get_shifts_by_date(id,date)
    return render_template('restaurant_dayview.html', id=id, shifts=shifts, name=name, date=date)

@app.route("/restaurant/staff_strength_calendar")
def restaurant_staff_strength_calendar():
    week = request.args["week"]
    restaurantID = request.args["restaurantID"]
    calendar = restaurants.create_staff_strength_calendar(week,restaurantID)
    name = restaurants.get_name(restaurantID)
    return render_template("restaurant_staff_strength_calendar.html", calendar=calendar, week=week, name=name)

# Routes for forms

@app.route("/add/restaurant",methods=["GET","POST"])
def add_restaurant():
    if request.method == "GET":
        return render_template("add_restaurant.html")
    if request.method == "POST":
        name = request.form["name"]
        if restaurants.add_restaurant(name):
            id = restaurants.get_last_by_name(name)
            return redirect(url_for("restaurant", id=id))
        else:
            return render_template("error.html", message = "Ravintolan lisäys epäonnistui")

@app.route("/update/restaurant", methods=["GET","POST"])
def update_restaurant():
    if request.method == "GET":
        id = request.args.get("id")
        name = restaurants.get_name(id)
        return render_template("update_restaurant.html", id=id, name=name)
    if request.method == "POST":
        id = request.form["id"]
        new_name = request.form["new_name"]
        if restaurants.update_restaurant(id, new_name):
            # Lisää message / parempi route vielä
            return redirect(url_for('restaurant', id=id))
        else:
            return render_template("error.html", message = "Ravintolan muokkaus epäonnistui")


@app.route("/remove/restaurant", methods=["GET", "POST"])
def remove_restaurant():
    if request.method == "GET":
        id = request.args.get("id")
        name = restaurants.get_name(id)
        return render_template("remove_restaurant.html", id=id, name=name)
    if request.method == "POST":
        id = request.form["id"]
        if restaurants.remove_restaurant(id):
            # Lisää message / parempi route vielä
            return redirect("/")
        else:
            return render_template("error.html", message = "Ravintolan poisto epäonnistui")

@app.route("/restaurant/add/shift",methods=["GET","POST"])
def add_shift():
    if request.method == "GET":
        restaurantID = request.args.get("restaurantID")
        return render_template("add_shift.html", restaurantID=restaurantID)

    if request.method == "POST":
        name = request.form["name"]
        restaurantID = request.form["restaurantID"]
        role = request.form["role"]
        date = request.form["date"]
        start_time = request.form["start_time"]
        duration = request.form["duration"]
        reps = request.form["reps"]
        repetition = request.form["repetition"]
        if restaurants.add_shift(name, restaurantID, role, date, start_time, duration, reps,repetition):
            return redirect(url_for("restaurant", id=restaurantID))
        else:
            return render_template("error.html", message = "Työvuoron lisäys epäonnistui")


@app.route("/update/shift", methods=["GET","POST"])
def update_shift():
    if request.method == "GET":
        id = request.args.get("id")
        shift = restaurants.get_shift(id)
        name = shift[1]
        restaurantID = shift[2]
        role = shift[3]
        date = shift[4]
        start_time = shift[5]
        duration = shift[6]
        return render_template("update_shift.html", id=id,
                                                    name=name, 
                                                    restaurantID=restaurantID,
                                                    role=role,
                                                    date=date,
                                                    start_time=start_time,
                                                    duration=duration )

    if request.method == "POST":
        id = request.form["id"]
        new_name = request.form["new_name"]
        new_role = request.form["new_role"]
        new_date = request.form["new_date"]
        new_start_time = request.form["new_start_time"]
        new_duration = request.form["new_duration"]
        restaurantID = request.form["restaurantID"]
        if restaurants.update_shift(id, new_name, new_role, new_date, new_start_time, new_duration):
            # Lisää message / parempi route vielä
            return redirect(url_for('restaurant', id=restaurantID))
        else:
            return render_template("error.html", message = "Työvuoron muokkaus epäonnistui")

@app.route("/remove/shift", methods=["GET", "POST"])
def remove_shift():
    if request.method == "GET":
        id = request.args.get("id")
        shift = restaurants.get_shift(id)
        name = shift[1]
        date = shift[4]
        return render_template("remove_shift.html", id=id, name=name, date=date)
    if request.method == "POST":
        id = request.form["id"]
        if restaurants.remove_shift(id):
            # Lisää message / parempi route vielä
            return redirect("/")
        else:
            return render_template("error.html", message = "Työvuoron poisto epäonnistui")

@app.route("/restaurant/add/employee",methods=["GET","POST"])
def add_employee():
    if request.method == "GET":
        restaurantID = request.args.get("restaurantID")
        return render_template("add_employee.html", restaurantID=restaurantID)

    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]        
        restaurantID = request.form["restaurantID"]
        role = request.form["role"]
        max_hours = request.form["max_hours"]

        if restaurants.add_employee(firstname,lastname,restaurantID, role, max_hours):
            return redirect(url_for("restaurant", id=restaurantID))
        else:
            return render_template("error.html", message = "Työntekijän lisäys epäonnistui")


@app.route("/update/employee", methods=["GET","POST"])
def update_employee():
    if request.method == "GET":
        id = request.args.get("id")
        employee = restaurants.get_employee(id)
        return render_template("update_shift.html", employee=employee)

    if request.method == "POST":
        id = request.form["id"]
        new_firstname = request.form["new_firstname"]
        new_lastname = request.form["new_lastname"]
        new_role = request.form["new_role"]
        new_max_hours = request.form["new_max_hours"]
        restaurantID = request.form["restaurantID"]
        if restaurants.update_employee(id, new_firstname, new_lastname, new_role, new_max_hours):
            # Lisää message / parempi route vielä
            return redirect(url_for('restaurant', id=restaurantID))
        else:
            return render_template("error.html", message = "Työntekijän muokkaus epäonnistui")

@app.route("/remove/employee", methods=["GET", "POST"])
def remove_employee():
    if request.method == "GET":
        id = request.args.get("id")
        employee = restaurants.get_employee(id)
        firstname = employee[1]
        lastname = employee[2]
        return render_template("remove_employee.html",firstname=firstname,lastname=lastname, id=id)
    if request.method == "POST":
        id = request.form["id"]
        if restaurants.remove_employee(id):
            # Lisää message / parempi route vielä
            return redirect("/")
        else:
            return render_template("error.html", message = "Työntekijän poisto epäonnistui")

# Register/login/logout 

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Rekisteröinti ei onnistunut")


@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")
