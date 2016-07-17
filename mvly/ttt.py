#!/usr/bin/env python

import os
import urllib2
import json

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"),
    extensions=['jinja2.ext.autoescape'],
    autoescape=False)

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
