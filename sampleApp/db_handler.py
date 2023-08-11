from sampleApp import mysql


def save_user(form):
    name = form.get("name")
    email = form.get("email")
    roll = form.get("role")

    status = 1
    try:
        cur = mysql.connection.cursor()
        qry = "INSERT INTO users(`name`, `email`,`role`) VALUES(%s, %s, %s)"
        result = cur.execute(qry, (name, email, roll))
        mysql.connection.commit()
        if not result:
            status = "Failed to save user detail"
    except:
        status = "Sorry! Error encountered while saving user details"
    finally:
        cur.close()
    return status
