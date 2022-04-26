from app import *


class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True, server_default=text("nextval('songs_id_seq'::regclass)"))
    name = Column(Text, nullable=False)
    duration = Column(Time, nullable=False)
    release_year = Column(Integer, nullable=False)
    album_id = Column(ForeignKey('albums.id'))

    album = relationship('Album')
    users = relationship('User', secondary='users_songs') # secondary - attr for: users_songs connect to table
