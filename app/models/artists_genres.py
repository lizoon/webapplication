from app import *

t_artists_genres = Table(
    'artists_genres', Base.metadata,
    Column('artist_id', ForeignKey('artists.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
    Column('genre_id', ForeignKey('genres.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
)
