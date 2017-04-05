from helper_functions import *
from time import sleep

class scraper:
    """Basic web scraper built around urllib2.urlopen.

       Methods:
       __init__ - initialize the scraper with a list of websites
       scrape_all - activate the scraper
    """

    def __init__( self, site_list ):
        """Initialize scraper with a website list.

        site_list - a Python list of strings where each string is a URL
        """
        self.rem_sites = site_list
        self.err_sites = []

    def scrape_all( self, dest='./', delay=1 ):
        """Activate scraper.

        Keyword arguments:
        dest -- directory in which to store downloaded websites
        delay -- delay between requests for individual websites in seconds
        """
        sites = self.rem_sites
        while sites:
            site = sites.pop( )
            try:
                scrape_to( site, dest )
            except:
                self.err_sites.append( site )
            sleep( delay )
        print self.err_sites
