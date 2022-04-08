from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, Table, Text, Time, UniqueConstraint, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)


Base = declarative_base()
metadata = Base.metadata




