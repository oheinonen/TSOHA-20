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
            return redirect(url_for('restaurant_add_schedule', restaurantID=id, day_of_week=1))
        else:
            return render_template("error.html", message = "Ravintolan lisäys epäonnistui")

@app.route("/restaurant/<int:id>")
def restaurant(id):
    sql = "SELECT name FROM restaurants WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    name = result.fetchone()[0]
    sql = "SELECT day_of_week,time_start,working_time FROM schedules WHERE restaurantID=" + str(id)
    result = db.session.execute(sql)
    workdays = result.fetchall()
    return render_template("restaurant.html", id=id, name=name, workdays=workdays)

@app.route("/restaurant/<int:restaurantID>/add_schedule/<int:day_of_week>", methods= ["GET","POST"])
def restaurant_add_schedule(restaurantID,day_of_week):
    if request.method == "GET":
        return render_template("add_schedule.html", restaurantID=restaurantID, day_of_week=day_of_week)
    if request.method == "POST":
        time_start = request.form["time_start"]
        working_time = request.form["working_time"]
        if restaurants.add_schedule(day_of_week,time_start, working_time, restaurantID):
            if day_of_week == 7:
                return redirect(url_for('restaurant', id=restaurantID))
            else:
                day_of_week_next = day_of_week + 1
                return redirect(url_for('restaurant_add_schedule', restaurantID=restaurantID, day_of_week=day_of_week_next))
        else:
            return render_template("error.html", message = "Aikataulun lisäys epäonnistui")

@app.route("/restaurant/<int:restaurantID>/add_urgency_class/<int:classNro>", methods= ["GET","POST"])
def restaurant_add_urgency_class(restaurantID,classNro):
    if request.method == "GET":
        return render_template("add_urgency_class.html", restaurantID=restaurantID, classNro=classNro)
    if request.method == "POST":
        bakers = request.form["leipuri"]
        chefs = request.form["kokki"]
        waiters = request.form["tarjoilija"]
        cashiers = request.form["kassahenkilö"]
        dishwashers = request.form["tiskari"]
        if restaurants.add_urgency_class(bakers,chefs,waiters,cashiers,dishwashers, restaurantID):
            return redirect(url_for('restaurant', id=restaurantID))
        else:
            return render_template("error.html", message = "Kiireysluokan teko epäonnistui")


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
