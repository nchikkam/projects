import unittest

from lib.crawler import SiteMap
from urlparse import ParseResult

class SiteMapUnitTests(unittest.TestCase):

    def test_sitemap_instance_creation(self):
        """
            Verify that the creation of the sitemap works without arguments
        :return: None
        """
        site_map = SiteMap()
        self.assertEqual(site_map.site_map, {})
        self.assertEqual(site_map.network, {})
        self.assertEqual(site_map.unvisited, set([]))
        self.assertEqual(site_map.start_page, None)
        self.assertEqual(site_map.get_network_json_format(), '{}')

    def test_compose_url_from_hash_href(self):
        """
            Verify composing big urls based on domain and intra links work properly
        :return: None
        """
        href = "#intra-link"
        url = ParseResult(scheme='http', netloc='www.gc.com', path='', params='', query='', fragment='')
        actual = SiteMap().compose_url_from_href(url, href)
        expected = 'http://www.gc.com#intra-link'
        self.assertEqual(expected, actual)

    def test_compose_url_from_relative_link_href(self):
        """
            verifies that href relative links composition works fine.
        :return: None
        """
        href = "./intra-link"
        url = ParseResult(scheme='http', netloc='www.gc.com', path='', params='', query='', fragment='')
        actual = SiteMap().compose_url_from_href(url, href)
        expected = 'http://www.gc.com/intra-link'
        self.assertEqual(expected, actual)

    def test_compose_url_from_relative_startingwithslash_href(self):
        """
            verifies that href absolute composition works fine.
        :return: None
        """
        href = "/intra-link"
        url = ParseResult(scheme='http', netloc='www.gc.com', path='', params='', query='', fragment='')
        actual = SiteMap().compose_url_from_href(url, href)
        expected = 'http://www.gc.com/intra-link'
        self.assertEqual(expected, actual)

    def test_compose_url_from_relative_startingnotwith_http_href(self):
        """
            verifies that href composition works if the protocol schem is missing in the input parameters.
        :return: None
        """
        href = "/intra-link"
        url = ParseResult(scheme='', netloc='www.gc.com', path='', params='', query='', fragment='')
        actual = SiteMap().compose_url_from_href(url, href)
        expected = 'http://www.gc.com/intra-link'
        self.assertEqual(expected, actual)

    def test_compose_url_from_with_properurl(self):
        """
            verifies that href composition works if the protocol scheme is missing in the input parameters.
        :return: None
        """
        href = "http://www.gc.com"
        url = None
        actual = SiteMap().compose_url_from_href(url, href)
        expected = 'http://www.gc.com'
        self.assertEqual(expected, actual)

    def test_get_out_going_edges_works_fine(self):
        valid_links = [
            "http://nonexistingurl.com/about.html",
            "http://nonexistingurl.com/help.html",
            "./products.html",
            "/samples.html",
            "http://nonexistingurl.com/path?a=b#dummy"
        ]

        anchors = ""
        for link in valid_links:
            anchors += "<a href=\"{0}\">link</a>\n".format(link)

        html = "<html><body>{0}</body></html>".format(anchors)

        expected = [
            "http://nonexistingurl.com/about.html",
            "http://nonexistingurl.com/help.html",
            "http://nonexistingurl.com/products.html",
            "http://nonexistingurl.com/samples.html",
            "http://nonexistingurl.com/path",
        ]

        subject = SiteMap()
        subject.set_start_page("nonexistingurl.com")
        url = ParseResult(scheme='http', netloc='nonexistingurl.com', path='', params='', query='', fragment='')
        actual = subject.get_out_going_edges(url, html)
        for e in expected:
            self.assertTrue(e in actual)

if __name__ == "__main__":
    unittest.main()