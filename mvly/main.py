#!/usr/bin/env python

import os

import jinja2
import webapp2

from jsonparser import(
    JsonParserApp, JsonParser, ErrorHandler
)

from ttt import (
    TicTacToe, TicTacToe4x4
)

from urlshortener import (
    URLShortenerHandler, Redirecter
)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=False)


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