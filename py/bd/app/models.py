from app import db

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1024), index=True)

    def __repr__(self):
        return '<Text %r>' % (self.data)