#!/usr/bin/env python

import os
import jinja2
import webapp2

from lib.base62 import (
    Base62Util
)

from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=False)

URL_SHORTNER_NAME = 'url_shortener'     # key to thendb data store
baseUtil = Base62Util()                 # a utility class for encoding

def urldb_key(url_shortener=URL_SHORTNER_NAME):
    """
        We use url_shortener as the key, Entry as the value to hold urls
    """
    return ndb.Key('Entry', url_shortener)

class Entry(ndb.Model):
    """
        A table to store the original url and its mapping to shorened form
    """
    url = ndb.StringProperty(indexed=False)
    shortened = ndb.StringProperty(indexed=False)
    id = ndb.IntegerProperty()
    duration = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


"""
    This class handles the requests to urlshortenter.html.
    urlshortener must support both get and post methods. When the
    requested page is get, the normal page is displayed along with the
    urls that were requested so far and post handles the procesing of
    the new ones and storing them in the ndb datastore.
"""
class URLShortenerHandler(webapp2.RequestHandler):

    def get(self):
        """
            Method to handle the urlshortener app
        :return: rendered urlshortener html page
        """
        url_shortener = self.request.get('url_shortener',
                                          URL_SHORTNER_NAME)
        query = Entry.query(
            ancestor=urldb_key(url_shortener)).order(-Entry.date)

        rows = query.fetch(10)  # keep the limit to 10 entries

        template_values = {
            'entries': rows
        }

        template = JINJA_ENVIRONMENT.get_template('urlshortener.html')
        self.response.write(template.render(template_values))

    def post(self):
        """
            Method to handle the post requests that include the new long
            urls requested by users. This creates an entry into the  ndb
            data store and uses the rowID of the created antry as integer
            to convert it into base62 encoded string to use it as the
            shortened url. Later when users request these shortened urls
            a simple redirect is done with the Redirect Handler to process
            the requests and direct the users to the original Url.
        :return:
        """
        url_shortener = self.request.get('url_shortener',
                                          URL_SHORTNER_NAME)
        entry = Entry(parent=urldb_key(url_shortener))

        entry.url = self.request.get('url')
        entry.put()

        entry.shortened = baseUtil.toBase(entry.key.id())
        entry.id = entry.key.id()
        entry.put()

        # get all urls so far to display
        query = Entry.query(
            ancestor=urldb_key(url_shortener)).order(-Entry.date)

        rows = query.fetch(10)  # keep the limit to 10 entries

        template_values = {
            'entries': rows
        }

        template = JINJA_ENVIRONMENT.get_template('urlshortener.html')
        self.response.write(template.render(template_values))


"""
    Handler to just redirect the users who come with shoretened urls
    to the original ones. This just does a base62 decoding of the shortened
    url, uses the resultant value as entry into the ndb data store, retrives
    the origianl url and redirect the user to that page.
"""
class Redirecter(webapp2.RequestHandler):
    def get(self):
        """
            Redirects the user to the original page, after retrieving the
            original url using the base62 decoding mechanism.
        :return: None
        """
        base62Encoded = self.request.get('t')
        id = int(baseUtil.toDec(base62Encoded))

        query = Entry.query(Entry.id == id)
        rows = query.fetch(10)

        self.redirect(str(rows[0].url))
