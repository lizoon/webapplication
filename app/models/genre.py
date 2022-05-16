from app import *


class Genre(db.Model):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True, server_default=text("nextval('genres_id_seq'::regclass)"))
    name = Column(String(15), nullable=False)

    def __repr__(self):
        return f'{self.name}'

