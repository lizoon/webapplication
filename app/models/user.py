from app import *


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, server_default=text("nextval('users_id_seq'::regclass)"))
    nickname = Column(String(15), nullable=False)
    password = Column(String(80), nullable=False)
    email = Column(String(30), nullable=False)
    gender = Column(String)


def __init__(self, nickname, password, email, gender):
        self.nickname = nickname
        self.password = password
        self.email = email
        self.gender = gender
