from flask import render_template
from app import app
from flask.ext.mysql import MySQL

mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

@app.route('/')
@app.route('/index')
def index():
    cursor.execute("SELECT * FROM Notebook")
    data = cursor.fetchall()[0:30]
    user = { 'nickname': 'Andrii' }
    posts = [
        {
            'author' : {'nickname' : 'John'},
            'body' : 'Title one'
        },
        {
            'author' : {'nickname' : 'Mike'},
            'body' : 'Big step in life'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        posts = posts,
        user = user,
        data = data)
