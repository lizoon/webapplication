from app import *
from app.models.genre import Genre


class Artist(db.Model):
	__tablename__ = 'artists'
	__table_args__ = (UniqueConstraint('firstname', 'surname'),)

	id = Column(Integer, primary_key=True, server_default=text("nextval('artists_id_seq'::regclass)"))
	firstname = Column(String(25), nullable=False)
	surname = Column(String(25))
	genre_id = Column(ForeignKey('genres.id', ondelete='SET NULL'), nullable=False)

	genre = relationship('Genre')

	def __repr__(self):
		if self.surname != None:
			return f'{self.firstname} {self.surname}'
		return f'{self.firstname}'

