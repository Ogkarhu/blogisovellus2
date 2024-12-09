from flask import Flask
from flask import render_template, request, session, redirect
from app import app
from db import db
from sqlalchemy.sql import text



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