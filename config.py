import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = False

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:x3nonx4@localhost/karwan'

DEBUG = True

HOST = '0.0.0.0'

SECRET_KEY="dfsdfsdf"

MEDIA_FOLDER = os.path.join(basedir, 'app/static/')
MEDIA_URL = '/static/'

ADMINS = frozenset(['youremail@yourdomain.con'])
