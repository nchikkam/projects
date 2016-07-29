from urllib2 import urlopen                 # library to request url(s)
from urlparse import (                      # parsing tools for urls, to extract path, query, fragments etc
    urlparse,
    urldefrag
)
import json
import logging
from robotparser import RobotFileParser

from util import timeit
from bs4 import BeautifulSoup               # HTML could be messy so using regexes might not work for some cases,
                                            # using this parser is better than regex and custom parsing.

"""
    This class encompasses different methods so as to generate a site map for a given URL.
    Basically it supports following methods along with their abstract descriptions:
    1. __init__(...)               : constructor to initialize the members
    2. generate(...)               : the invoker method that actually starts generation of site map
    3. write_to_file(...)          : helper method to cast the collected details into file.
    4. compose_url_from_href(...)  : cleans the href attribute values and creates correct form of the urls.
    5. get_out_going_links(...)    : creates a list of links that are emanating from currently given page.
    6. record_visit(...)           : creates entries into the table dictionary for later usage.
    7. get_static_assets(...)      : static assets of a page could be .css, .js, .img or .mp4 links this creates
                                     a seperate list for each one of them and populates the dictionary.
    8. crawl(...)                  : main driver method that crawls the page recursively.
"""
class SiteMap():

    def __init__(self, main_page=None, robotrules=True):
        """
            Constuctor method that initializes the members that are used during crawling process
        :param main_page: The root page that needs to be crawled for generation of sitemap
        """

        logging.info("Consider Robot.txt ? ==> "+str(robotrules))
        self.robotrules = robotrules
        self.site_map = {}                          # map that records the visits of urls, datemodified and assets
        self.network = {}                           # map that maintains the network/graph of webpages visited
                                                    # The intention of this map is for visual rendering using d3.js

        self.unvisited = set([])                    # a set to keep the list of urls yet to be visited
        self.start_page = None                       # the root page, this is used to avoid cycle and keeping crawl
                                                    # process limited to single domain.
        self.robot_txt_rules = None

        if main_page:
            self.unvisited.add(main_page)
            try:
                self.start_page = urlparse(main_page).netloc
            except:
                logging.error("Improper URL, Please provide a Valid Url:"+main_page)
                exit(0)

        if self.robotrules == "True":
            try:
                logging.info("robot.txt respected")
                self.robot_txt_rules = RobotFileParser()
                self.robot_txt_rules.set_url(main_page + "/robots.txt")
                self.robot_txt_rules.read()
            except:
                logging.error("Unable to read the robot.txt file")
                self.robotrules = False # error reading robot.txt, ignore it forever

    @timeit
    def generate(self, site_map=None):
        """
            This method holds the invoking control of the crawler method and drives the crawling process.
            Basically a BFS style method that keeps popping the elements from the queue [self.unvisited set]
            and scraping the urls.

            Once the crawling process is done, this creates sitemap using the self.site_map dictionary with
            just url, date-modified tags with dummy frequency and priorities.
        :param site_map: name of the site_map file so as to create xml entries.
        :return:
        """
        while self.unvisited:
            self.crawl()
        # create xml from the site_map dictionary
        header = """<?xml version="1.0" encoding="UTF-8"?>
            <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
            xmlns:xhtml="http://www.w3.org/1999/xhtml"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
        """
        footer = """\n</urlset>\n"""
        entry = "\t<url>\n\
                 \t\t<loc>%s</loc>\n\
                 \t\t<lastmod>%s</lastmod>\n\
                 \t\t<changefreq>monthly</changefreq>\n\
                 \t\t<priority> 1 </priority>\n\
                 \t</url>\
        "

        xml = header
        for url in self.site_map.keys():
            xml += entry % (url, self.site_map[url]['date']) + "\n"

        xml += footer
        if site_map != None:
            self.write_to_file(site_map, xml)
        else:
            self.write_to_file("sitemap.xml", xml)
        return xml

    def write_to_file(self, file_name, content):
        """
            A utility method to just write the contents of the file into a given file name.
            Alert: This overwrites if the file does exist in the current directory.
        :param file_name: name of the file, sitemap in our case.
        :param content:   contents of the file
        :return: None
        """
        f = open(file_name, 'w')
        f.write(content)
        f.close()

    def compose_url_from_href(self, url, href):
        """
            There are different ways a href could specify a location and it varies in different ways based on how
            the page is designed. This method takes few styles into consideration and ignores some, cleans and creates
            a valid url link so as to keep it ready for the crawl method.
        :param url:   basae url of the current page
        :param href:  one of the hyper links of the page
        :return:      a well formed and valid http link
        """
        if href.startswith('/'):
            return "http://%s%s"%(url.netloc, href)
        elif href.startswith('#'):
            return "http://%s%s%s"%(url.netloc, url.path, href)
        elif href.startswith('./'):
            return "http://%s%s"%(url.netloc, href[1:])
        elif not href.startswith('http'):
            return "http://" + url.netloc + '/' + href

        return href

    def get_out_going_edges(self, url, html_body):
        """
            This method encompasses the BFS along with the coupling with crawl and generator as it changes the state
            of the unvisited map. Basically this method extracts the links that belong to the same domain as the start
            page, cleans them with compose_url_from_href method and updates the map. This also avoids unnecessary traps
            like href links pointing to 'javascript', 'mailto' etc.
        :param url:         current page url
        :param html_body:   current page's html content
        :return:            returns all the valid and wellformed out going links from this page
        """
        soup = BeautifulSoup(html_body, "html.parser")
        valid_links_for_this_page = []
        for a in soup.find_all('a', href=True):

            href = a['href']
            href = self.compose_url_from_href(url, href.decode("utf-8"))

            # clean the href so that it will have legitimate urls instead of #cluttered ones and q=param prints
            href = urldefrag(href)[0]  # skip intra links [this took time to find out !] ##1
            # remove query params as only the path matters
            if href.find('?') != -1:
                href = href[:href.find('?')]  ##2

            new_page = urlparse(href)

            # add to the queue only it it doesn't cause a cycle
            # assumption: if a link ends with gocardless.com, assuming it can be crawled to make sitemap complete
            if  not str(new_page.netloc).endswith(self.start_page):          # doesn't belong to domain
                continue

            if  self.robot_allows(href) and \
                not href in self.site_map.keys()            and \
                not href in self.unvisited                  and \
                not 'javascript:' in href                   and \
                not 'mailto:' in href:
                self.unvisited.add(href)
                valid_links_for_this_page.append(href)

        return valid_links_for_this_page

    def record_visit(self, url, headers, html_body):
        """
            Any time a specific url of a site is changed, its last-modified date and time are kept in the page headers.
            This info helps bots and crawlers to not to crawl the page if it has not been updated since last crawl.
            This method is used to preserve the url crawled and its last-modified time along with assets scraped into
            the container dictionary for later usage to generate sitemap and visualization network.
        :param url:         url of the just finished crawling page
        :param headers:     header information of the crawled page
        :param html_body:   html content of the page
        :return:            None
        """
        if 'last-modified' in headers:
            date = headers['Last-Modified']
        else:
            date = headers['Date']

        self.site_map[url] = {
            'date': date,
            'assets': self.get_static_assets(html_body)
        }

    def get_static_assets(self, html_body):
        """
            A html page could contain other links such as .css, .img. .mp4 and .js. All these files are not dynamic
            though they could produce dynamic results. The code or text that exists in these files is constant and
            static. These files are referred as static assets and for the definition of this challenge, I have chosen
            to keep all the info in a single dictionary and extract them at the end for reports, results and stats.
        :param html_body:       html content of the page.
        :return:                returns a dictionary that encompasses .css, .img, ijs files as lists.
        """
        # add static assets of the page .css, .js and image urls may be ?
        soup = BeautifulSoup(html_body, "html.parser")
        img = soup.findAll("img")
        css = soup.findAll("link", {"rel": "stylesheet"})

        # js is tricky: I faced an issue with inline javascript and ignoring it for the time being.
        # an extract like html_body with just needed parts is a must for excluding inline scripts and styles.
        jss = []
        for x in soup.findAll('script'):
            try:
                list.append(x['src'])
            except KeyError:
                pass

        csss = []
        imgs = []
        jss = []
        for link in css:
            csss.append(link['href'])
        for link in img:
            imgs.append(link['src'])
        for link in jss:
            jss.append(link['src'])

        return {
                'css': csss,
                'img': imgs,
                'js':  jss
        }

    def crawl(self):
        """
            The main driver method that crawls the pages. This main does below steps:
            for every unvisited [vertex|page] that belongs to the requested domain:
                crawl the page
                record valid links and their last-modified-dates
        :return:   None
        """
        page = self.unvisited.pop()
        # if robot.txt is defined, use Disallow to avoid pages. gocardless.robot.txt doesn't exist so the crawler
        # must find all the pages for report.
        logging.info("Starting to Crawl Page: " + page)

        url = urlparse(page)
        try:
            response = urlopen(page)
        except:
            logging.debug("Issue with the url: " + page)
            return None
        try:
            html_body = response.read() # response.getcode()
            response.close()
            # record visit ans assets
            self.record_visit(page, response.headers, html_body)
            logging.debug("Queued Pages: {0}, Crawled Pages: {1}".format(len(self.unvisited), len(self.site_map)))
        except:
            logging.debug("Issue while opening url: " + page)
            return None
        connects = self.get_out_going_edges(url, html_body)

        # simple Graph that keeps the order of the pages crawled.
        for i, url in enumerate(connects):
            self.network[page] = {
                'to': connects,
                'assets': {
                    'css': self.site_map[page]['assets']['css'],
                    'js':  self.site_map[page]['assets']['js'],
                    'img': self.site_map[page]['assets']['img']
                }
            }
        return None

    def get_site_map(self):
        """
            Returns the compiled sitemap structure
        :return:       sitemap data structure
        """
        return self.site_map

    def get_network_graph(self):
        """
            Returns the compiled network in the order of the crawled pages
        :return:       network graph
        """
        return self.network

    def get_network_json_format(self):
        """
            Returns the crawl traverse order sequence in json format
        :return:       network in json format
        """
        return json.dumps(self.network)

    def set_start_page(self, url):
        """
            This could be useful if one is testing
        :param url: start page to start the crawling.
        :return:
        """
        self.start_page = url

    def robot_allows(self, link):
        if not self.robotrules: return True
        try:
            if self.robot_txt_rules.can_fetch("*", link):
                    return True
            return False
        except:
            return True
