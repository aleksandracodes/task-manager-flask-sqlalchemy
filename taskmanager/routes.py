from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
# this is our home page
def home():
    return render_template("tasks.html")