from flask import Flask
from flask.ext.mysql import MySQL

app = Flask(__name__)
from app import views

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'andrew05'
app.config['MYSQL_DATABASE_DB'] = 'notebookDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
