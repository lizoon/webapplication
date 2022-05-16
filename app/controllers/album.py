from app import *
from app.models.user import *
from app.models.users_songs import *


@app.route('/album/<album_id>')
@login_required
def album(album_id):
    album = Album.query.get(album_id)
    songs = Song.query.filter(Song.album_id == album_id).all()
    return render_template('album.html', title='album', artist=album.name, songs=songs)

