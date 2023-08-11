from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sampleApp'
app.config['SECRET_KEY'] = "ourGreatSecretKey"

mysql = MySQL(app)

import sampleApp.routs
