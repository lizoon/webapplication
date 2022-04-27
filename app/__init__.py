from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Configuration
from sqlalchemy import MetaData, Column, ForeignKey, Integer, Table, Text, Time, String, Boolean, text
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


Base = declarative_base()

app = Flask(__name__, template_folder='templates')
app.config.from_object(Configuration)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

bootstrap = Bootstrap(app)

from app.controllers import user
