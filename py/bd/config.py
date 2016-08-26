import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

SQLALCHEMY_DATABASE_URI = "postgres://test:test@127.0.0.1:5433/test"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
