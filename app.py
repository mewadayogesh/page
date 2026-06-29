from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    # TODO: Add your authentication logic here
    error = "Invalid username or password"
    return render_template("login.html", error=error)

if __name__ == "__main__":
    app.run()
