import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = False

# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'pymysql://root:x3nonx4@localhost/karwan'

DEBUG = True

HOST = '0.0.0.0'

ADMINS = frozenset(['youremail@yourdomain.con'])
