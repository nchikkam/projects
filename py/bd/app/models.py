from app import db


class Result(db.Model):
    __tablename__ = 'results'

    id =        db.Column(db.Integer, primary_key=True)
    url =       db.Column(db.String())

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url

    def __repr__(self):
        return '<id {}>'.format(self.id)