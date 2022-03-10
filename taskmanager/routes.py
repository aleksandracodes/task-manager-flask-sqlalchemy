from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
# this is our home page
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():  # these are Python functions, not route names
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])  # both methods needed as we'll be submitting the data to the database
def add_category():
    return render_template("add_category.html")