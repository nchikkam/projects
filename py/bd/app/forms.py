from flask.ext.wtf import Form
from wtforms import StringField, validators

class BigDataStoreForm(Form):
    search_word = StringField('Video Search', [validators.DataRequired()])