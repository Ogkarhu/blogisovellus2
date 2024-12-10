from flask import Flask
from flask import render_template, request, session, redirect
from app import app
from db import db
from sqlalchemy.sql import text




def like():
        
    
    if request.method == "POST":
        post_id = request.form["post_id"]

        check = text("SELECT EXISTS(SELECT FROM likes WHERE user_id = :user_id AND post_id = :post_id )")
        liked = db.session.execute(check, {"user_id": session["user_id"], "post_id": post_id}).fetchone()
        if not liked[0]:
            query = text("INSERT INTO likes (user_id, post_id) VALUES (:user_id, :post_id)")
            db.session.execute(query, {"user_id": session["user_id"], "post_id": post_id})
            db.session.commit()
        else:
            query = text("DELETE FROM likes WHERE user_id = :user_id AND post_id = :post_id")
            db.session.execute(query, {"user_id": session["user_id"], "post_id": post_id})
            db.session.commit()

        return redirect(request.referrer)
    
def get_like():
    sql = text("""SELECT P.id,
            COUNT(L.likes) AS likes,
            ARRAY_AGG(array[C.id::varchar(255), C.comment]) AS comments
            FROM posts AS P
            JOIN users AS U ON P.user_id = U.id
            LEFT JOIN comments AS C ON C.post_id=P.id
            LEFT JOIN likes as L ON L.post_id=P.id
            WHERE P.user_id=U.id
            GROUP BY P.id
            ORDER BY P.id
            """)
    posts = db.session.execute(sql)
    return posts.fetchall()