
from app.app import app
#from flask.ext.sqlalchemy import SQLAlchemy

if __name__ == '__main__':
#    app.config.from_object('config')
#    db = SQLAlchemy(app)

    app.run(debug=True)
