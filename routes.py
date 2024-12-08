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
import like
import follows

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
        admin = request.form.get("admin")
        if admin is None:
            admin = False
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if users.register(username, password1, admin):
            return redirect("/login")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")

@app.route("/")
def index():
    post_list= posts.get_list()
    print(post_list)
    return render_template("index.html", posts=post_list)

@app.route("/logout")
def logout():
    users.logout()
    return render_template("login.html")


@app.route("/like", methods =["POST"])
def like_route():
    like.like()
    return redirect("/")

@app.route("/follows", methods =["GET","POST"])
def follow_route():
    if request.method == "POST":
        follows.follow()
        all_users = users.userlist()
        return redirect("/follows")
    if request.method == "GET":
        all_users = follows.not_followed()
        followed = follows.followed()
        return render_template("followed.html", users= all_users, followed= followed)
    
@app.route("/own_feed")
def own_feed():
    post_list= posts.get_list()
    follower = list(map(lambda x:x[0],follows.follower()))
    all_users = users.userlist
    post_list = [p for p in post_list if p.username in follower]
    return render_template("own_feed.html", posts = post_list, all_users = all_users, follower = follower )
