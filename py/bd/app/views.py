from flask import render_template, request, jsonify
from app import app
from .forms import (
    BigDataStoreForm
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


BigData = [
    { 'data': "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."},
    { 'data': "To be fond of dancing was a certain step towards falling in love."},
    { 'data': "Jane Austen was an English novelist known primarily for her six major novels which interpret, critique and comment upon the life of the British landed gentry at the end of the 18th century"},
    { 'data': "travelling, skiing, swimming, hockey, cricket are sports"},
    { 'data': "target.com is an online competitor"},
    { 'data': "Amazon supports online selling and buying for retail business by hosting an online platform on a cloud."},
    { 'data': "Google is a search based company, they crawl all the pages on internet at specified frequencies and use pagerank alogorithm to rank the pages."}
]


@app.route('/')
def home_page():
    return "Home Page"

@app.route('/us/rawdata/1.0/searchitems', methods=['GET', 'POST'])
@requires_auth
def searchitems():
    form = BigDataStoreForm()
    if request.method == 'GET':
        data = BigData
        return render_template('restservice.html',
                               title='Rest Service',
                               form=form,
                               searchitems=data)
    elif request.method == 'POST':
        search_word = request.form['search_word']
        records =  []
        for record in BigData:
            if search_word in record['data']:
                records.append(record)

        return render_template('restservice.html',
                               title='Rest Service',
                               form=form,
                               searchitems=records)

@app.route('/us/rawdata/1.0/searchitems/<int:top_limit>', methods=['GET'])
@requires_auth
def search_top_limit_items(top_limit):
    form = BigDataStoreForm()
    data = BigData[:top_limit]
    return render_template('restservice.html',
                           title='Rest Service',
                           form=form,
                           searchitems=data)