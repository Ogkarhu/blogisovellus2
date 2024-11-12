from flask import Flask
from flask import render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from app import app
from db import db

def get_list():
    sql = "SELECT M.content, U.username, M.sent_at FROM posts M, users U" \
          "WHERE M.user_id=U.id ORDER BY M.id"
    result = db.session.execute(sql)
    return result.fetchall()
