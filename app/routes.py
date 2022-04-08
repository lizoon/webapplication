from app import *


@app.route('/')
def hello_world():
    #new_album = Album(name='Hello', release_year=2002)
    #db.session.add(new_album)
    #db.session.commit()

    # results = db.session.query(Album).all()
    # for r in results:
    #     print(r.name)
    return 'Hello World!'

