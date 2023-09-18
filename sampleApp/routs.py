from flask import render_template, request, redirect, url_for, flash
from sampleApp import app
import sampleApp.db_handler as dbh
from sampleApp.Forms import AddEmployeeForm


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home_page.html")


@app.route("/hello")
def hello_page():
    return render_template('hello_page.html')


@app.route("/adduser", methods=["GET", "POST"])
def adduser_page():
    form = AddEmployeeForm()
    if form.validate_on_submit():
        dataSaveStatus = dbh.save_user(request.form)
        if dataSaveStatus:
            return redirect(url_for("users_page"))
        else:
            return f'<h2 class="text-danger">{dataSaveStatus}</h2>'
    return render_template("adduser_page.html", form=form)


@app.route("/users")
def users_page():
    users = dbh.getAllUsersDetails()
    return render_template("users_page.html", users=users)


@app.route("/users/<int:uid>")
def user_detail(uid):
    user = dbh.getUserDetails(id=uid)
    # print("from route : ",user)
    return render_template("user_detail.html" , user=user , id=uid)


@app.route("/delete/<int:uid>") 
def delete_user(uid):
    status = dbh.deleteUserDetails(uid)
    flash(f"Status of deletion of user with id {uid} : {status}")
    return redirect(url_for("users_page"))
