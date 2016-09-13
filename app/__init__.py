from flask import Flask

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'andrew05'
app.config['MYSQL_DATABASE_DB'] = 'notebookDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


from app import views
