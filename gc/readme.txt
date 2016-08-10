1. Project Title: Simple Web Crawler
----------------------------------------------------------------------------------
Description: 
	This is a small crawler project, given a URL, this crawler crawls the main 
	page, scrapes the out going url links, does a bit of cleanup so that crawling 
	will not happen on other domains, invalid links, links pointing to the same 
	page with '#'s and so on. Once the crawling process finishes, it creates a .xml 
	file with all the valid links that are reachable from the main page along with 
	its last-modified-date. The crawler assumes that the frequency of the pages is 
	'monthly' and a priority of 1 for all.

	The .json artifact produced contains the assets for each page along with the
	traversed order used by the Crawler.

	Packages and Notes:
	+ The code is written using 2.7 python version.
	+ In order to run this project, a bs4 [BeautifulSoup] package must be installed.

2. Project Directory Structure:
----------------------------------------------------------------------------------
crawler:


.	+------ design					(design diagrams, usecases and typical look of 
.	|															assets json files)
.	+------ library                 (library to hold the actual SiteMap class and 
.	|									util that casts time taken by the whole 
.	|																		Process)
.	|
.	+------ sample_outputs          (For demo purposes, sample sitemaps of two sites
.	|															 were included.)
.	|																
.	+------ crawler.py      		(This is the library module that hold the logic 
.	|														and class for site map)
.	|
.	+------ crawlertests.py 		(Testing methodology for the crawler module. Any 
.	|									addition to crawler, must have a test 
.	|										here. In fact, test must be written 
.	|										before method.)
.	|
.	+------ main.py 				(Command line launcher for the crawler module)
.	|
.	+------ readme.txt 				(Textual description of this project, file itself)


3. Steps to run the launcher:
----------------------------------------------------------------------------------
	C:\python27\python.exe main.py --rooturl http://gc.com --sitemapxml gc.xml --sitemapjson gc.json <ENTER>

4. Artifacts that the project produces:
----------------------------------------------------------------------------------
	|
	|
	+------- gc.xml         (sitemap.xml file for the gc domain)
	|
	+------- gc.json        (sitemap.json file for the gc domain, 
										the idea was to use a visualization library 
										such as d3 to generate visual sitemap)

Additional Notes: 
----------------------------------------------------------------------------------
	.xml file will contain only the loc, date modified, frequency and priority tags.
	.json file will expose the assets such as .css, .img and .js files for each of the url.
	A UML and Sequence diagram could be found in the same folder where this readme.txt resides.


Challenges: 
----------------------------------------------------------------------------------
+ Most of the URL(s) were having Fragments, i.e URL(s) with '#somestring' postfix 
  that refer to the subsection of the same page.

+ Some URL(s) have query parameters with "query_name=query_value" format in the urls. 
  Only hostname + path must be considered for crawling, as there could be many URL(s) 
  with this kind of pattern.

+ How to go about crawling the pages when the launch page doesn't expose the 'robot.txt'.
  Especially during a simple test, gc.com is missing this resrouce file.

+ What if the html has .js content and this javascript composes the http href links on
  demand, but these urls doesn't exist when the page gets launched initially. 
		+ Considering this .js which generates the href links is out of the scope of a 
		  small project as it needs a java script interpreter and presentation logic 
		  that generates the actual .html that is needed to parse finally. This is 
		  still an open challenge to take it further.

+ Depth to consider while crawling. The dfs approach might lead to infinite recursion, 
  so a BFS approach was chosen, which always makes sure that the stack overflow error
  will not occur.

+ A thought of attempting a set of retries, incase if the url responses are not being 
  served properly by the servie. This could be an extension.



Sample Runs Used During Development and Testing:
----------------------------------------------------------------------------------
C:\Python27\python.exe main.py --rooturl http://demosite.com --sitemapxml gc.xml --sitemapjson gc.json --robotrules False
C:\Python27\python.exe main.py --rooturl http://anotherdemo.com --sitemapxml sitemap_json.xml --sitemapjson sitemap_json.json --robotrules False

