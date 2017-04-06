"""Helper Functions for Web Scraping Module

scrape_to - download a page
validate_path - make sure path exists
"""

from urllib2 import urlopen

def path_validate(path):
    """Make sure a path exists and is correctly formatted.
    """
    # functionality to be added later
    return path

def scrape_to(str, dest):
    """Download a website specified by URL str to a directory specified by dest.
    """
    dest = path_validate(dest)
    site = urlopen(str)
    site_content = site.read()
    full_path = dest+str.replace('/', '.')+'.txt'
    site_file = open(full_path, 'w')
    site_file.write(site_content)
    site_file.close()
    return
