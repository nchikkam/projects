#!/usr/bin/env python

import os
import urllib

from google.appengine.ext import ndb

import jinja2
import webapp2

from lib.base62 import (
    Base62Util
)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

URL_SHORTNER_NAME = 'url_shortener'
baseUtil = Base62Util()

def urldb_key(url_shortener=URL_SHORTNER_NAME):
    """
        We use url_shortener as the key.
    """
    return ndb.Key('Entry', url_shortener)

class Entry(ndb.Model):
    url = ndb.StringProperty(indexed=False)
    shortened = ndb.StringProperty(indexed=False)
    id = ndb.IntegerProperty()
    duration = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):

    def get(self):
        url_shortener = self.request.get('url_shortener',
                                          URL_SHORTNER_NAME)
        query = Entry.query(
            ancestor=urldb_key(url_shortener)).order(-Entry.date)

        rows = query.fetch(10)

        template_values = {
            'entries': rows
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

class URLShortenerHandler(webapp2.RequestHandler):

    def get(self):
        url_shortener = self.request.get('url_shortener',
                                          URL_SHORTNER_NAME)
        query = Entry.query(
            ancestor=urldb_key(url_shortener)).order(-Entry.date)

        rows = query.fetch(10)

        template_values = {
            'entries': rows
        }

        template = JINJA_ENVIRONMENT.get_template('urlshortener.html')
        self.response.write(template.render(template_values))

    def post(self):
        url_shortener = self.request.get('url_shortener',
                                          URL_SHORTNER_NAME)
        entry = Entry(parent=urldb_key(url_shortener))

        entry.url = self.request.get('url')
        entry.put()

        entry.shortened = baseUtil.toBase(entry.key.id())
        entry.id = entry.key.id()
        entry.put()

        query_params = {'url_shortener': url_shortener}
        self.redirect('/?' + urllib.urlencode(query_params))

class Redirecter(webapp2.RequestHandler):
    def get(self):
        base62Encoded = self.request.get('t')
        id = int(baseUtil.toDec(base62Encoded))

        query = Entry.query(Entry.id == id)
        rows = query.fetch(10)

        self.redirect(str(rows[0].url))

class TicTacToe(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('ttt.html')
        self.response.write(template.render({}))

class JsonResumeParser(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('jsonparser.html')
        self.response.write(template.render({}))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/shorten', URLShortenerHandler),
    ('/r', Redirecter),
    ('/ttt', TicTacToe),
    ('/jsonparser', JsonResumeParser),
], debug=True)