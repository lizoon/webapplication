from app import *


class Album(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True, server_default=text("nextval('albums_id_seq'::regclass)"))
    name = Column(Text, server_default=text("'New Album'::text"))
    release_year = Column(Integer)
    artist_id = Column(ForeignKey('artists.id'))

    artist = relationship('Artist') # add attrs to models для доступа к данным, (name of responsible class for ONE relation)

    def __init__(self, name, release_year, artist_id):
        self.name = name
        self.release_year = release_year
        self.artist_id = artist_id

    def __repr__(self):
        return f'{self.name} i am from {self.release_year}'
