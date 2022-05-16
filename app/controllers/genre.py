from app import *
from app.models.user import *
from app.models.users_songs import *


@app.route('/genre/<genre_id>')
def genre(genre_id):
    genre = Genre.query.get(genre_id)
    artists = Artist.query.with_entities(Artist.firstname,
                                         Artist.surname,
                                         Artist.id).filter(Artist.genre_id == genre_id).all()
    return render_template('genre.html', title='genre', genre=genre.name, artists=artists)

