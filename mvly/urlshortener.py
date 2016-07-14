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
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
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

    def post(self):
        url_shortener = self.request.get('url_shortener',
                                          URL_SHORTNER_NAME)
        entry = Entry(parent=urldb_key(url_shortener))

        entry.url = self.request.get('url')
        entry.put()

        entry.shortened = baseUtil.toBase(entry.key.id())
        entry.put()

        query_params = {'url_shortener': url_shortener}
        self.redirect('/?' + urllib.urlencode(query_params))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/shorten', URLShortenerHandler),
], debug=True)