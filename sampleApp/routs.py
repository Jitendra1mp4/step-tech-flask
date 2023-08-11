from flask import render_template, request,flash,redirect, url_for
from sampleApp import app
import sampleApp.db_handler as dbh


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home_page.html")


@app.route("/hello")
def hello_page():
    return "<h1>Hello World!</h1>"


@app.route("/adduser", methods=["GET", "POST"])
def adduser_page():
    if request.method == "POST":
        print(request.form)
        status = dbh.save_user(request.form)
        if status: 
            return redirect(url_for('users_page'))
        else:
            return f'<h2 class="text-danger">{status}</h2>'
    return render_template("adduser_page.html")


@app.route("/users")
def users_page():
    return render_template("users_page.html")


@app.route("/user/<username>")
def user_detail(username):
    return render_template("user_detail.html", username=username)
