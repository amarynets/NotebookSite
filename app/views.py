from app import app

@app.route("/")
def hello():
    return "Hello, world!"

if __name__ == "__main__":
    app.run()
