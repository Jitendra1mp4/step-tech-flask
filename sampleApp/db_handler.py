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


def getAllUsersDetails() : 
    status = 1
    try:
        cur = mysql.connection.cursor()
        qry = "SELECT * FROM users"
        cur.execute(qry)
        rs = cur.fetchall()
        return rs 
    except:
        status = "Sorry! Error encountered while retrieving user details"
    finally:
        cur.close()
    return status


def getUserDetails(id) : 
    status = 1
    try:
        cur = mysql.connection.cursor()
        qry = f"SELECT * FROM users where id={id}"
        # print(qry)
        cur.execute(qry)
        rs = cur.fetchone()
        # print("rs fjd 1 ", rs[1])
        return rs 
    except:
        status = "Sorry! Error encountered while retrieving user details"
    finally:
        cur.close()
    return status