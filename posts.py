from flask import Flask
from flask import render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from db import db
from sqlalchemy import text

def get_list():
    sql = text(
      "SELECT  P.id, P.body, P.youtube_url, P.created_at\
      FROM posts P, users U \
      WHERE P.user_id=U.id ORDER BY P.id")
    result = db.session.execute(sql)
    return result.fetchall()
