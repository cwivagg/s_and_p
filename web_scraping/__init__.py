"""Initialize the web_scraping module.

   Modules used:
   scraper - a simple wrapper for urllib2 to download websites
   site_parser - a simple wrapper for lxml to parse html websites
   helper_functions - accessory functions for the scraper and parser modules
"""

from . import scraper
from . import site_parser
from . import helper_functions
