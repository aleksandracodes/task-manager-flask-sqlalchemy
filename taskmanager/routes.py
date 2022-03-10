from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():  # these are Python functions, not route names
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)
    # first 'categories' is the variable name used in html template,
    # second 'categories' is a variable defined in the function above

@app.route("/add_category", methods=["GET", "POST"])
# both methods needed as we'll be submitting the data to the database
def add_category():
    if request.method == "POST":
        # remember to import the request, redirect, url_for methods from Flask at the top
        category = Category(category_name=request.form.get("category_name"))  # retrieve name attribute
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")  # update category name
        db.session.commit()  # commit the session to our database
        return redirect(url_for("categories"))  # redirect the user back to the categories section
    return render_template("edit_category.html", category=category)