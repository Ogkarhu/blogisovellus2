from flask import Flask
from flask import render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from db import db
from sqlalchemy import text

#def get_list():
#    sql = text(
#      "SELECT  P.id, P.body, P.youtube_url, P.created_at\
#      FROM posts P, users U \
#      WHERE P.user_id=U.id \
#      ORDER BY P.id")
#    result = db.session.execute(sql)
#    return result.fetchall()

def get_list():
  sql = text("""SELECT P.id,
             P.body,
             P.youtube_url,
             P.created_at,
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