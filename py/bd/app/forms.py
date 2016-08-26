from flask.ext.wtf import Form
from wtforms import StringField, validators

class BigDataStoreForm(Form):
    search_word = StringField('Data Search', [validators.DataRequired()])