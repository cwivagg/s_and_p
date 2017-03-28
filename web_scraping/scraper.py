from helper_functions import *

from time import sleep
        
# Scraper Class
#   instantiates with websites to be downloaded
# Methods
#   scrape_all - scrapes websites in queue to directory and with optional
#                time lag

class scraper:

    def __init__( self, site_list ):
        self.rem_sites = site_list
        self.err_sites = []

    def scrape_all( self, dest='./', delay=1 ):
        sites = self.rem_sites
        while sites:
            site = sites.pop( )
#            try:
            scrape_to( site, dest )
#            except:
#                self.err_sites.append( site )
            sleep( delay )
