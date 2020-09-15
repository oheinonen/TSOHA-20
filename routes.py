from app import app
from flask import render_template, request, redirect
from db import db
import users, restaurants

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/restaurant/<int:pk>/add_employee",methods=["GET","POST"])
# def add_employee():
#    if request.method == "GET":
#        return render_template("add_employee.html" )
#    if request.method == "POST":
#        name = request.form["name"]
#        max_hours = request.form["hours"]
#        role = request.form["role"]
#        restaurantID = request.form["restaurantID"]

@app.route("/add/restaurant",methods=["GET","POST"])
def add_restaurant():
    if request.method == "GET":
        return render_template("add_restaurant.html")
    if request.method == "POST":
        id = request.form["id"]
        name = request.form["name"]
        if restaurants.add_restaurant(name):
            return render_template("/restaurant.html", name=name, restaurantID=id)
        else:
            return render_template("error.html", message = "Ravintolan lisäys epäonnistui")

@app.route("/restaurant/<int:id>")
def restaurant(id):
    sql = "SELECT name FROM restaurants WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    name = result.fetchone()[0]
    return render_template("restaurant.html", id=id, name=name)


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
