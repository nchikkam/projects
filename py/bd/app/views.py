from flask import render_template, request, jsonify
from app import app
from .forms import (
    BigDataStoreForm
)
from .models import BigData

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

@app.route('/us/rawdata/1.0/searchitems', methods=['GET', 'POST'])
@requires_auth
def searchitems():
    form = BigDataStoreForm()
    if request.method == 'GET':
        data = BigData.query.all()
        return render_template('restservice.html',
                               title='Rest Service',
                               form=form,
                               searchitems=data)
    elif request.method == 'POST':
        search_word = request.form['search_word']
        data = BigData.query.filter(BigData.data.contains(search_word)).all()
        return render_template('restservice.html',
                               title='Rest Service',
                               form=form,
                               searchitems=data)

@app.route('/us/rawdata/1.0/searchitems/<int:top_limit>', methods=['GET'])
@requires_auth
def search_top_limit_items(top_limit):
    form = BigDataStoreForm()
    from .models import BigData

    print (top_limit)
    data = BigData.query.limit(top_limit).all()
    return render_template('restservice.html',
                           title='Rest Service',
                           form=form,
                           searchitems=data)