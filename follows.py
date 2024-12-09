from flask import Flask
from flask import render_template, request, session, redirect
from app import app
from db import db
from sqlalchemy.sql import text

from users import user_id


def follow():
    if request.method == "POST":
        followed_id = request.form["followed_id"]
        #username = request.form["username"]
        check = text("SELECT EXISTS(SELECT FROM follows WHERE follower_id = :follower_id AND followed_id = :followed_id )")
        following = db.session.execute(check, {"follower_id": session["user_id"], "followed_id": followed_id}).fetchone()[0]
        print(following)
        print(followed_id)
        if not following:
            query = text("INSERT INTO follows (follower_id, followed_id) VALUES (:follower_id, :followed_id)")
            db.session.execute(query, {"follower_id": session["user_id"], "followed_id": followed_id})
            db.session.commit()
        # else:
        #     query = text("DELETE FROM likes WHERE user_id = :user_id AND post_id = :post_id")
        #     db.session.execute(query, {"user_id": session["user_id"], "post_id": post_id})
        #     db.session.commit()    
    

def followed():
    user = user_id()
    sql = text("SELECT users.username FROM users LEFT JOIN follows ON followed_id = users.id WHERE follower_id = :user")
    followed = db.session.execute(sql, {"user": user})
    return followed

def not_followed():
    user = user_id()
    sql = text("""SELECT username, id, is_admin FROM users U LEFT JOIN follows F ON F.followed_id=U.id AND F.follower_id=:user WHERE F.follower_id IS NULL""")
    followed = db.session.execute(sql, {"user": user})
    return followed

def follower():
    user = user_id()
    sql = text("SELECT users.username FROM users LEFT JOIN follows ON follower_id = users.id WHERE follower_id = :user")
    follower = db.session.execute(sql, {"user": user})
    return follower