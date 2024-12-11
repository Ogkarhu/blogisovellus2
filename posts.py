from flask import Flask
from flask import render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from db import db
from sqlalchemy import text

def get_list():
  sql = text("""SELECT P.id,
             P.body,
             P.youtube_url,
             P.created_at,
             U.username,
             U.id,
             (SELECT count(*) FROM likes WHERE post_id=P.id) AS likes,
             ARRAY_AGG(array[C.id::varchar(255), C.comment,U2.username]) AS comments
             FROM posts AS P
             JOIN users AS U ON P.user_id = U.id
             LEFT JOIN comments AS C ON C.post_id=P.id
             LEFT JOIN users as U2 ON U2.id = C.user_id
             WHERE P.user_id=U.id
             GROUP BY P.id, U.username, U.id
             ORDER BY P.id
             """)
  posts = db.session.execute(sql)
  return posts.fetchall()