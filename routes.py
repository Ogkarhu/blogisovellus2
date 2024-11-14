from flask import Flask
from app import app
from flask import render_template, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
import users
import new_post
import posts
import comments
import new_comment



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/login")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

@app.route("/")
def index():
    post_list= posts.get_list()
    post_and_comment=[]
    for post in post_list:
        post_dict = dict(post._mapping)
        comment_list= comments.get_list(post_dict["id"])
        post_dict["comments"] = comment_list
        post_and_comment.append(post_dict)
    print(post_and_comment)
    return render_template("index.html", posts=post_and_comment)

@app.route("/logout")
def logout():
    users.logout()
    return render_template("login.html")

@app.route("/new_comment")
def new_comment_route():
    new_comment.add_comment()
    return render_template("/")