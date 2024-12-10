from flask import Flask
from flask import render_template, session, request, redirect
from flask_sqlalchemy import SQLAlchemy
from db import db
from app import app
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
import secrets


def login(username, password):
    sql = text("SELECT id, password, is_admin FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = username
            session["is_admin"] = user.is_admin
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False

def user_id():
    return session.get("user_id", 0)

def logout():
    session = None

def register(username, password, admin):
    hash_value = generate_password_hash(password)
    try:
        sql = text("INSERT INTO users (username, password, is_admin) VALUES (:username, :password, :is_admin)")
        db.session.execute(sql, {"username":username, "password":hash_value, "is_admin": admin})
        db.session.commit()
    except:
        return False
    return login(username, password)

def userlist():
    user = user_id()
    sql = text("SELECT username, id, is_admin FROM users WHERE users.id <> :user")
    all_users = db.session.execute(sql, {"user" :user})
    return all_users


