from flask import Flask
from sqlalchemy.sql import text
from app import app
from db import db
from flask import render_template, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
import users
import posts
import comments
import like
import follows
import utils

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
    if not session:
        return redirect("/login")
    users.logout()
    return render_template("login.html")


@app.route("/like", methods =["POST"])
def like_route():
    if not session:
        return redirect("/login")
    utils.csrf()
    like.like()
    return redirect(request.referrer)

@app.route("/follows", methods =["GET","POST"])
def follow_route():
    if not session:
        return redirect("/login")
    if request.method == "POST":
        utils.csrf()
        print(request.form)
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
    follower = list(map(lambda x:x[0],follows.followed()))
    all_users = users.userlist
    post_list = [p for p in post_list if p.username in follower]
    return render_template("index.html", own_feed = True, posts = post_list, all_users = all_users, follower = follower )

@app.route("/new_comment", methods=["POST", "GET"])
def add_comment():
    if not session:
        return redirect("/login")
    if request.method == "GET":
        return render_template("/")
    if request.method == "POST":
        utils.csrf()
        post_id = request.form["post_id"]
        comment = request.form["comment"]
        if comment.strip() == "":
            return render_template("error.html", message = "viesti ei voi olla tyhjä")
        else:
        # Insert post (comment and YouTube link) into the database
            query = text("INSERT INTO comments (user_id, comment, post_id) VALUES (:user_id, :comment, :post_id)")
            db.session.execute(query, {"user_id": session["user_id"], "comment": comment, "post_id": post_id})
            db.session.commit()

        return redirect(request.referrer)
    
@app.route("/new_post", methods=["POST", "GET"])
def add_video():
    if not session:
        return redirect("/login")
    if request.method == "GET":
        return render_template("new_post.html")
    
    content = request.form["content"]
    link = request.form.get("link", "")

    youtube_url = None

    if "youtube.com/watch?v=" in link:
        index = link.find("v=") + 2
        endindex = link.find("&", index)
        unique = link[index:endindex] if endindex != -1 else link[index:]
        youtube_url = f"https://www.youtube.com/embed/{unique}"
    elif "youtu.be/" in link:
        # Extract video ID
        unique = link.split("youtu.be/")[1]
        youtube_url = f"https://www.youtube.com/embed/{unique}"
    else:
        return redirect("/")

    # Insert post (comment and YouTube link) into the database
    query = text("INSERT INTO posts (user_id, body, youtube_url) VALUES (:user_id, :content, :youtube_url)")
    db.session.execute(query, {"user_id": session["user_id"], "content": content, "youtube_url": youtube_url})
    db.session.commit()

    return redirect("/")