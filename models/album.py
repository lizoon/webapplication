from app.app import *


class Album(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True, server_default=text("nextval('albums_id_seq'::regclass)"))
    name = Column(Text, server_default=text("'New Album'::text"))
    release_year = Column(Integer)
    artist_id = Column(ForeignKey('artists.id'))

    artist = relationship('Artist')
