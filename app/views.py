from flask import render_template
from app import app
from flask.ext.mysql import MySQL

mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM Notebook")
    data = cursor.fetchall()[0:30]
    hello = "List with scrap info:"
    return render_template("index.html",
        hello = hello,
        data = data)
