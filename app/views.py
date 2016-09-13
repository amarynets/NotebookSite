from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
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
        user = user)
