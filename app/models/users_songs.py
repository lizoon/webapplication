from app import *

t_users_songs = Table(
    'users_songs', db.Model.metadata,
    Column('user_id', ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
    Column('song_id', ForeignKey('songs.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
)
