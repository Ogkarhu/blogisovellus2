from flask import Flask
from flask import render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from db import db
from sqlalchemy import text

def get_list(post_id):
    sql = text(
      "SELECT  C.id, C.comment, C.sent_at\
      FROM comments C, users U \
      WHERE C.user_id=U.id \
      AND \
      C.post_id=:post_id\
      ORDER BY C.id")
    result = db.session.execute(sql,{"post_id":post_id})
    return result.fetchall()