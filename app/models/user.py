from app import *
from flask_security import UserMixin, RoleMixin


t_roles_users = Table(
    'roles_users', db.Model.metadata,
    Column('role_id', ForeignKey('roles.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
    Column('user_id', ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
)


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, server_default=text("nextval('roles_id_seq')"))
    name = Column(String(15), nullable=False, unique=True)
    description = Column(String(255))


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, server_default=text("nextval('users_id_seq')"))
    password = Column(String, nullable=False)
    email = Column(String(60), nullable=False)
    nickname = Column(String(20), nullable=False)
    active = Column(Boolean())

    roles = relationship('Role', secondary=t_roles_users, backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return f'{self.nickname}'
