from app import *


class Artist(Base):
	__tablename__ = 'artists'
	__table_args__ = (UniqueConstraint('firstname', 'surname'),)

	id = Column(Integer, primary_key=True, server_default=text("nextval('artists_id_seq'::regclass)"))
	firstname = Column(Text, nullable=False)
	surname = Column(Text)

	genres = relationship('Genre', secondary='artists_genres')
