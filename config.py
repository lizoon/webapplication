class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://localhost:5432/laba"
    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
