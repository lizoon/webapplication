from app import *


class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True, server_default=text("nextval('genres_id_seq'::regclass)"))
    name = Column(String(15), nullable=False)

