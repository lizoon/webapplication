from app import *


class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True, server_default=text("nextval('genres_id_seq'::regclass)"))
    name = Column(Text, nullable=False)

