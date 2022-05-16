from app import *
from app.models.user import *
from app.models.users_songs import *
from itertools import groupby


@app.route('/artist/<artist_id>')
@login_required
def artist(artist_id):
    artist = Artist.query.get(artist_id)
    albums = Album.query.filter(Album.artist_id == artist_id).all()
    return render_template('artist.html',
                           title='search_artist',
                           artist=artist.firstname
                           if artist.surname == None
                           else f'{artist.firstname} {artist.surname}',
                           albums=albums)


@app.route('/artists')
@login_required
def artists():
    return render_template('artists.html', title='', func=fav_artist, flag=False)


def fav_artist(flag):
    user_id = current_user.id
    songs = db.session.query(Song).filter(Song.users.any(User.id == user_id))
    albums = []
    artists = []
    for song_ in songs:
        album_ = (db.session.query(Album).get(song_.album_id))
        albums.append(album_)

    for album_ in albums:
        artist_ = db.session.query(Artist).filter(Artist.id == album_.artist_id).first()
        artists.append(artist_)

    if not flag:
        return set(artists)

    artists_new = {}

    for artist_ in artists:
        count = artists.count(artist_)
        artists_new.update({artist_: count})

    sorted(artists_new.items(), key=lambda kv: kv[1], reverse=True)

    if len(artists_new.values()) == 0:
        return []
    elif len(artists_new.values()) < 4:
        return artists_new.keys()
    else:
        return list(artists_new.keys())[:4]
