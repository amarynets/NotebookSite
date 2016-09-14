from flask import render_template
from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
mysql.init_app(app)


@app.route('/')
def index():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM notebook")
    data = cursor.fetchall()[0:30]

    cursor.close()
    conn.close()

    hello = "List with scrap info:"
    return render_template("index.html",
        hello = hello,
        data = data)

