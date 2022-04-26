from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Configuration
from sqlalchemy import MetaData, Column, ForeignKey, Integer, Table, Text, Time, UniqueConstraint, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

