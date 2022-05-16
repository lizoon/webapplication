from flask import Flask, render_template, abort, redirect, url_for, request, session, flash

from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import MetaData, Column, ForeignKey, Integer, Table, Text, Time, String, Boolean, text, UniqueConstraint,\
    Numeric, CheckConstraint, DateTime
from sqlalchemy.orm import relationship

from flask_admin import Admin, AdminIndexView, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user, login_user, logout_user

from datetime import timedelta

from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder='templates')
app.config.from_object(Configuration)

db = SQLAlchemy(app)


from app.models.user import User, Role
from app.models.artist import Artist
from app.models.song import Song
from app.models.genre import Genre
from app.models.album import Album


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))


# клас для ограничения админки вьюх
class AdminView(AdminMixin, ModelView):
    pass


# home view admin
class HomeAdminView(AdminMixin, AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('sequrity/index.html')


admin = Admin(app, 'FlaskApp', url='/homepage', index_view=HomeAdminView(name='Home'), template_mode='bootstrap3')
bootstrap = Bootstrap(app)


admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Artist, db.session))
admin.add_view(AdminView(Song, db.session))
admin.add_view(AdminView(Genre, db.session))
admin.add_view(AdminView(Album, db.session))


from app.controllers import album
from app.controllers import artist
from app.controllers import genre
from app.controllers import song
from app.controllers import user


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=25)


