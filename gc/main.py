import argparse
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from lib.crawler import SiteMap

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Generate Sitemap for a give URL')

    parser.add_argument('--rooturl', help='the main webpage to start the sitemap generation')
    parser.add_argument('--sitemapxml', help='generate the sitemap xml for the url')
    parser.add_argument('--sitemapjson', help='generate the sitemap json for the url')
    parser.add_argument('--robotrules', help='ignore the robot.txt rules if it\'s there')

    args = parser.parse_args()

if  args.rooturl and args.sitemapxml and args.sitemapjson:
    c = SiteMap(args.rooturl, args.robotrules)
    c.generate(args.sitemapxml)
    c.write_to_file(args.sitemapjson, c.get_network_json_format())
else:
    logging.info("Please pass all the positional Arguments and try again.")
