import os
basedir = os.path.abspath(os.path.dirname(__file__))

if 'DATABASE_URL' not in os.environ:
	os.environ['DATABASE_URL'] = "postgres://test:test@127.0.0.1:5433/test"

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']