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