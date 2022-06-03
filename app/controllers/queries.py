from app import *
from app.models.user import *
from app.models.users_songs import *
from sqlalchemy.sql import func

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, Regexp


class Query23(FlaskForm):
    firstname = StringField('Ім\'я артиста',
                            validators=[InputRequired(message='Ім\'я не має бути порожнім!')])
    surname = StringField('Прізвище артиста')


class Query36(FlaskForm):
    nickname = StringField('Нікнейм',
                           validators=[InputRequired(message='Ім\'я не має бути порожнім!'),
                                       Length(min=4, max=15, message='Довжина імені має бути від 4 до 15 символів!'),
                                       Regexp('[a-z A-Z а-я А-Я 0-9]+', message='Ім\'я має містити букви!')])

    email = StringField('Пошта',
                        validators=[Length(max=30, message='Занадто довга поштова скринька!'),
                                    Email(message='Пошта має бути заповнена!'),
                                    Regexp('^[a-z A-Z 0-9 ]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$',
                                           message='Не валідний емейл!!'), ])


class Query4(FlaskForm):
    genre = StringField('Жанр', validators=[InputRequired(message='Введіть назву жанру!')])


@app.route('/show_query/<id_>', methods=['POST', 'GET'])
@login_required
def show(id_):
    form23 = Query23()
    form36 = Query36()
    form4 = Query4()

    if id_ == '0':
        keys_artist = db.session.query(Artist).with_entities(Artist.id).all()
        keys_artist = [i[0] for i in keys_artist]
        return render_template('queries.html',
                               title='queries',
                               keys_artist=keys_artist)

    a_1, u_2, a_3, a_4, a_5 = [], [], [], [], []
    # 1
    if id_ == '1':
        artist_id = request.form.get('comp_select')
        a_1 = db.session.query(Album).with_entities(Album.name).filter(Album.artist_id == artist_id).all()
        a_1 = [i[0] for i in a_1]
        if not a_1:
            return render_template('show_query.html', id='0')

    # 2
    if id_ == '2':
        a_name, a_surname = request.form['a_name'], request.form['a_surname']
        if a_name != '' or (a_name and a_surname != ''):
            artist_id = db.session. \
                query(Artist). \
                with_entities(Artist.id). \
                filter((Artist.firstname == a_name and Artist.surname == a_surname) \
                       or (Artist.firstname == a_name and Artist.surname is None)).all()
            if not artist_id:
                return render_template('show_query.html', id='0')

            artist_id = int(*artist_id[0])

            uu = (db.session.query(t_users_songs.columns.user_id).
                  join(Song, Song.id == t_users_songs.columns.song_id).
                  join(Album, Album.id == Song.album_id).
                  join(Artist, Artist.id == Album.artist_id).
                  filter(Artist.id == artist_id).group_by(t_users_songs.columns.user_id).
                  having(func.sum(Artist.id) >= 1)
                  ).all()

            for i in [i[0] for i in uu]:
                u_2.append(*(db.session.query(User).
                             with_entities(User.nickname).
                             filter(User.id == i).all())[0])
        else:
            return render_template('show_query.html', id='0')

    # 3
    if id_ == '3':
        u_name, u_email = request.form['u_name'], request.form['u_email']
        user_id = db.session.query(User.id).\
            filter(User.nickname == u_name
                   and User.email == u_email).all()
        if not user_id:
            return render_template('show_query.html', id='0')

        user_id = int(*user_id[0])

        aa = (db.session.query(Artist.id).
              join(Album, Album.artist_id == Artist.id).
              join(Song, Song.album_id == Album.id).
              join(t_users_songs, Song.id == t_users_songs.columns.song_id).
              join(User, User.id == t_users_songs.columns.user_id).
              filter(User.id == user_id)).group_by(Artist.id).all()

        for i in [i[0] for i in aa]:
            a_3.append(*(db.session.query(Artist).
                with_entities(Artist.firstname, Artist.surname).
                     filter(Artist.id == i).all()))
        for index, i in enumerate(a_3):
            if i[1] is None:
                i = [i[0]]
                a_3[index] = i
            else:
                i = [i[0], i[1]]
                a_3[index] = i

    # 4
    if id_ == '4':
        g_name = request.form['g_name']
        genre_id = (db.session.query(Genre.id).filter(Genre.name == g_name).all())
        if not genre_id:
            return render_template('show_query.html', id='0')
        genre_id = int(*genre_id[0])

        gg = (db.session.query(Genre.id).
              filter(Genre.id == genre_id).all())

        gg = int(*(gg)[0])
        a_4.append((db.session.query(Artist).
                     with_entities(Artist.firstname, Artist.surname).
                     filter(Artist.genre_id != gg).all()))
        a_4 = a_4[0]

        for index, i in enumerate(a_4):
            if i[1] is None:
                i = [i[0]]
                a_4[index] = i
            else:
                i = [i[0], i[1]]
                a_4[index] = i
    # 5
    if id_ == '5':
        n = int(request.form['n'])

        aa = db.session.query(Song.album_id).\
            group_by(Song.album_id).\
            having(func.count(Song.id)>n).all()
        if not aa:
            return render_template('show_query.html', id='0')

        for i in [i[0] for i in aa]:
            a_5.append(*(db.session.query(Album).
                       with_entities(Album.name).
                       filter(Album.id == i).all()[0]))

    return render_template('show_query.html',
                           title='query',
                           id=id_,
                           a_1=a_1,
                           u_2=u_2,
                           a_3=a_3,
                           a_4=a_4,
                           a_5=a_5)


@app.route('/show_query_2/<id_>', methods=['POST', 'GET'])
@login_required
def show_(id_):
    u_1, u_2, a_3 = [], [], []
    #1
    if id_ == '6':
        u_name, u_email = str(request.form['u_name']), str(request.form['u_email'])

        uu1 = db.session.query(Artist.id). \
            join(Album, Album.artist_id == Artist.id). \
            join(Song, Song.album_id == Album.id). \
            join(t_users_songs, t_users_songs.columns.song_id == Song.id). \
            join(User, t_users_songs.columns.user_id == User.id).\
            filter(User.nickname == u_name, User.email == u_email). \
            group_by(Artist.id)
        if not uu1:
            return render_template('show_query.html', id='0')

        u_1.append(db.session.query(User). \
                   with_entities(User.nickname, User.email). \
                   join(t_users_songs, t_users_songs.columns.user_id == User.id). \
                   join(Song, Song.id == t_users_songs.columns.song_id). \
                   join(Album, Album.id == Song.album_id). \
                   join(Artist, Artist.id == Album.artist_id). \
                   group_by(User.nickname, User.email). \
                   having(func.count(Artist.id) == uu1.count()).
                   filter(User.nickname != u_name and User.email != u_email).all())
        u_1 = [[i[0], i[1]] for i in (u_1[0])]

    # 2
    if id_ == '7':
        uu2 =db.session.query(Artist.id).\
            join(Album, Album.artist_id == Artist.id).\
            join(Song, Song.album_id == Album.id).\
            group_by(Artist.id)
        if not uu2:
            return render_template('show_query.html', id='0')

        u_2.append(db.session.query(User).\
            with_entities(User.nickname, User.email).\
            join(t_users_songs, t_users_songs.columns.user_id == User.id).\
            join(Song, Song.id == t_users_songs.columns.song_id).\
            join(Album, Album.id == Song.album_id).\
            join(Artist, Artist.id == Album.artist_id).\
            group_by(User.nickname, User.email).\
            having(func.count(Artist.id) == uu2.count()).all())
        u_2 = [*(u_2[0])[0]]

    # 3
    if id_ == '8':
        a_firstname, a_surname = str(request.form['a_firstname']), str(request.form['a_surname'])
        aa = db.session.query(Song.duration).\
            join(Album, Album.id == Song.album_id).\
            join(Artist, Artist.id == Album.artist_id).\
            filter(Artist.firstname == a_firstname and Artist.surname == a_surname).all()
        if not aa:
            return render_template('show_query.html', id='0')

        aa = [i[0] for i in aa]
        print(aa)
        for i in aa:
            a_3.append(db.session.query(Artist).
                   with_entities(Artist.firstname, Artist.surname).
                   join(Album, Album.artist_id == Artist.id).
                   join(Song, Song.album_id == Album.id).
                   filter(Song.duration == i).
                   filter( (Artist.firstname != a_firstname)).
                   group_by(Artist.firstname, Artist.surname).
                   all())
        x = []
        for i in a_3:
            for ii in i:
                x.append(ii)
        a_3 = x
    return render_template('show_query.html',
                           title='query',
                           id=id_,
                           u_1=u_1,
                           u_2=u_2,
                           a_3=a_3)
