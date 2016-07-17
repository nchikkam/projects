#!/usr/bin/env python


import os
import urllib2
import json

from google.appengine.ext import ndb

import jinja2
import webapp2

from lib.base62 import (
    Base62Util
)

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
    The Maing Handler class to launch the main page when users
    request the home page.
"""
class MainPage(webapp2.RequestHandler):

    def get(self):
        """
            Standard method to handle the get requests.
        :return: rendered index html page
        """
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({}))

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

"""
    This class handles the requests to play tic tac toe 3x3 version.
"""
class TicTacToe(webapp2.RequestHandler):
    def get(self):
        """
            Renders the game html page
        :return: None
        """
        template = JINJA_ENVIRONMENT.get_template('ttt.html')
        self.response.write(template.render({}))

"""
    This class handles the requests to play tic tac toe 4x4 version.
"""
class TicTacToe4x4(webapp2.RequestHandler):
    def get(self):
        """
            Renders the game html page
        :return: None
        """

        template = JINJA_ENVIRONMENT.get_template('ttt4x4.html')
        self.response.write(template.render({}))

"""
    This class holds the handling logic of the json resume parser app.
    Supports the get request and just renders the basic skeleton page
    that allows the user to choose a kind of  parsing  technique  and
    renders the resultant page using the selected choice.
"""
class JsonParserApp(webapp2.RequestHandler):
    def get(self):
        """
            Renders the basic app home page
        :return: None
        """

        template = JINJA_ENVIRONMENT.get_template('jsonparserapp.html')
        self.response.write(template.render({}))


"""
    This class Handles the actual processing of the user submitted .json
    url into a .html page using the selected choice.
"""
class JsonParser(webapp2.RequestHandler):

    def jsondata(self, jsonUrl):
        """
            This converts the given .json url content into an object to manage.
        :param jsonUrl: A publicly available .json file that contains resume content.
        :return: json parsed data as json object.
        """
        res = urllib2.urlopen(jsonUrl)
        data = json.load(res)
        return data

    def post(self):
        """
            This method holds the logic to process the given .json url
            using the method chosen by the user.
        :return: None
        """

        jsonUrl = self.request.get('jsonUrl')
        parsertype = self.request.get('parsertype')


        try:
            jsonData = self.jsondata(jsonUrl)
            if parsertype == "PureJson":
                cleanData = jsonData.__str__().replace("u\"","\"").replace("u\'","\'")
                template_values = {
                    'json': cleanData
                }

                template = JINJA_ENVIRONMENT.get_template('purejson.html')
                self.response.write(template.render(template_values))

            elif parsertype == "Python":

                template_values = {
                    'resume': jsonData,
                    'exps':   jsonData['experience']['items'],
                    'opensources': ["%s, %s"%(a,b) for a,b in jsonData['opensource']],
                    'talents': "  ".join(jsonData['header']['talents'])
                }

                template = JINJA_ENVIRONMENT.get_template('jsonpyparser.html')
                self.response.write(template.render(template_values))

            elif parsertype == "Python(Theme-Paper)":

                template_values = {
                    'resume': jsonData,
                    'exps': jsonData['experience']['items'],
                    'opensources': [[a, b] for a, b in jsonData['opensource']],
                    'talents': "  ".join(jsonData['header']['talents'])
                }

                template = JINJA_ENVIRONMENT.get_template('jsonpyfparser.html')
                self.response.write(template.render(template_values))


            elif parsertype == "javascript(d3)":
                template_values = { 'jsonUrl': jsonUrl }

                template = JINJA_ENVIRONMENT.get_template('jsonparser.html')
                self.response.write(template.render(template_values))
        except:
            template_values = {'error': "Invalid Json URL"}
            template = JINJA_ENVIRONMENT.get_template('jsonparserapperror.html')
            self.response.write(template.render(template_values))


"""
    Common page to cast all errors in Apps
"""
class ErrorHandler(webapp2.RequestHandler):
    def get(self):
        """
            Renders Error Page
        :return: None
        """
        template = JINJA_ENVIRONMENT.get_template('jsonparserapperror.html')
        self.response.write(template.render({}))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/urlshortener', URLShortenerHandler),
    ('/r', Redirecter),
    ('/ttt', TicTacToe),
    ('/ttt4x4', TicTacToe4x4),
    ('/jsonparserapp', JsonParserApp),
    ('/jsonparser', JsonParser),
    ('/error', ErrorHandler)
], debug=False)