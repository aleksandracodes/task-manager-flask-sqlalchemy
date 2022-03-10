# from flask import render_template, request, redirect, url_for
# from taskmanager import app, db
# from taskmanager.models import Category, Task


# @app.route("/")
# # this is our home page
# def home():
#     return render_template("tasks.html")


# @app.route("/categories")
# def categories():  # these are Python functions, not route names
#     return render_template("categories.html")


# @app.route("/add_category", methods=["GET", "POST"]) 
# # both methods needed as we'll be submitting the data to the database
# def add_category():
#     if request.method == "POST":
#         # remember to import the request, redirect, url_for methods from Flask at the top
#         category = Category(category_name=request.form.get("category_name"))  # retrieve name attribute
#         db.session.add(category)
#         db.session.commit()
#         return redirect(url_for("categories"))
#     return render_template("add_category.html")


    



from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")