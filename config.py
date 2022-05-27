class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://localhost:5432/laba"
    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
    FLASK_ADMIN_SWATCH = 'cerulean'
    SECURITY_PASSWORD_SALT = 'secret_salt'
    DB_HOST = 'localhost'
    DB_NAME = 'laba'
    DB_USER = 'liza'
    DB_PASS = 'liza'
