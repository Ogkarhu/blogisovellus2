from flask import Flask
from flask import render_template, request, session, redirect
from app import app
from db import db
from sqlalchemy.sql import text



@app.route("/new_comment", methods=["POST", "GET"])
def add_comment():
    if not session:
        return redirect("/login")
    if request.method == "GET":
        return render_template("/")
    if request.method == "POST":
        post_id = request.form["post_id"]
        comment = request.form["comment"]
        print(request.form)



        # Insert post (comment and YouTube link) into the database
        query = text("INSERT INTO comments (user_id, comment, post_id) VALUES (:user_id, :comment, :post_id)")
        db.session.execute(query, {"user_id": session["user_id"], "comment": comment, "post_id": post_id})
        db.session.commit()

        return redirect(request.referrer)