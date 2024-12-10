from flask import Flask
from flask import render_template, session, request, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from db import db
from app import app
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
import secrets

def csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)