import os
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "secret":
            flash(u"Dados inválidos", "error")
        else:
            flash(u"Login realizado com sucesso!")
            return redirect(url_for("index"))
    return render_template("login.html", error=error)


@app.errorhandler(404)
def not_found(error):
    return render_template("not_found.html"), 404


@app.errorhandler(500)
def server_error(error):
    return render_template("server_error.html"), 500
