from flask.ext.wtf import Form
from wtforms import StringField

class WeatherDataStoreForm(Form):
    search_word = StringField('Weather Search')

class AudioDataStoreForm(Form):
    search_word = StringField('Audio Search')

class VideoDataStoreForm(Form):
    search_word = StringField('Video Search')