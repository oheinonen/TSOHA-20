from app import app
from flask import render_template, request, redirect,session, url_for
from db import db
import users, restaurants

@app.route("/")
def index():
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
    sql = "SELECT name FROM restaurants WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    name = result.fetchone()[0]
    sql = "SELECT name,date, start_time, duration FROM shifts WHERE restaurantID=" + str(id)
    result = db.session.execute(sql)
    shifts = result.fetchall()
    return render_template("restaurant.html", id=id, name=name, shifts=shifts)

@app.route("/restaurant/<int:id>/add/shift",methods=["GET","POST"])
def add_shift(id):
    if request.method == "GET":
        return render_template("add_shift.html")
    if request.method == "POST":
        name = request.form["name"]
        role = request.form["role"]
        date = request.form["date"]
        start_time = request.form["start_time"]
        duration = request.form["duration"]
        if restaurants.add_shift(name, id, role,date, start_time, duration):
            return redirect(url_for("restaurant", id=id))
        else:
            return render_template("error.html", message = "Työvuoron lisäys epäonnistui")

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
