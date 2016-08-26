from flask import render_template, request, jsonify
from app import app
from .forms import (
    VideoDataStoreForm,
    AudioDataStoreForm,
    WeatherDataStoreForm
)
from functools import wraps

def check_auth(username, password):
    return username == 'dummy' and password == 'dummy'

def authenticate():
    message = {'message': "Authentication."}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()

        elif not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/service')
@requires_auth
def api_service():
    return "Service are available"

@app.route('/services')
@requires_auth
def api_services():
    return "Services are available"

@app.route('/weatherdatastore', methods=['GET', 'POST'])
def index():
    form = VideoDataStoreForm()
    if request.method == 'GET':
        return render_template('weatherdatastore.html',
                title='Weather Data Store',
                form=form)
    elif request.method == 'POST':
        search_word = request.form['search_word']
        #return search_word

        from .models import Weather
        import pdb
        pdb.set_trace()

        return str(Weather.query.all()[0])