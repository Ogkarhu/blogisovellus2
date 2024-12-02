from flask import Flask
from flask import render_template, request, session, redirect
from app import app
from db import db
from sqlalchemy.sql import text

def follow():
    if request.method == "POST":
        followed_id = request.form["username"]

        check = text("SELECT EXISTS(SELECT FROM follows WHERE follower_id = :follower AND followed_id = :followed_id )")
        following = db.session.execute(check, {"follower_id": session["user_id"], "followed_id": followed_id}).fetchone()
        if not following:
            query = text("INSERT INTO follows (follower_id, followed_id) VALUES (:follower_id, :followed_id)")
            db.session.execute(query, {"follower_id": session["user_id"], "followed_id": followed_id})
            db.session.commit()
        # else:
        #     query = text("DELETE FROM likes WHERE user_id = :user_id AND post_id = :post_id")
        #     db.session.execute(query, {"user_id": session["user_id"], "post_id": post_id})
        #     db.session.commit()    
    

def followed():
    pass