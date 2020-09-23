from app import app
from flask import render_template, request, redirect,session, url_for
from db import db
import users, restaurants

@app.route("/")
def index():
    # List all restaurants currently added to the website
    sql = "SELECT name,id FROM restaurants"
    result = db.session.execute(sql)
    restaurants = result.fetchall()
    return render_template("index.html", restaurants=restaurants)

@app.route("/add/restaurant",methods=["GET","POST"])
def add_restaurant():
    if request.method == "GET":
        return render_template("add_restaurant.html")
    if request.method == "POST":
        name = request.form["name"]
        if restaurants.add_restaurant(name):
            sql = "SELECT id  FROM restaurants WHERE name=:name ORDER BY id DESC LIMIT 1"
            result = db.session.execute(sql, {"name":name})
            id = result.fetchone()[0]
            return redirect(url_for("restaurant", id=id))
        else:
            return render_template("error.html", message = "Ravintolan lisäys epäonnistui")

@app.route("/restaurant/<int:id>")
def restaurant(id):

    # Name of the restaurant
    sql = "SELECT name FROM restaurants WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    name = result.fetchone()[0]

    # Shifts in this restaurant
    sql = "SELECT name,date, start_time, duration FROM shifts WHERE restaurantID=" + str(id)
    result = db.session.execute(sql)
    shifts = result.fetchall()

    # Employees in this restaurant
    sql = "SELECT firstname,lastname FROM employees WHERE restaurantID=" + str(id)
    result = db.session.execute(sql)
    employees = result.fetchall()

    return render_template("restaurant.html", id=id, name=name, shifts=shifts, employees=employees)

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
        if restaurants.add_shift(name, restaurantID, role,date, start_time, duration):
            return redirect(url_for("restaurant", id=restaurantID))
        else:
            return render_template("error.html", message = "Työvuoron lisäys epäonnistui")

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
