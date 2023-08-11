from flask import render_template, request
from sampleApp import app


@app.route("/")
# @app.route("/home")
def home_page():
    return render_template("home_page.html")


@app.route("/hello")
def hello_page():
    return "<h1>Hello World!</h1>"


@app.route("/users")
def users_page():
    return render_template("users_page.html")


@app.route("/user/<username>")
def user_detail(username):
    return render_template("user_detail.html", username=username)
