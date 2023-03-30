import os
from flask_sqlalchemy import SQLAlchemy
from src.app import app

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
connection = SQLAlchemy(app)