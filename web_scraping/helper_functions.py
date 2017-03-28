from urllib2 import urlopen

# Helper Functions
#   scrape_to     - downloads a page to the given directory
#   validate_path - makes sure path exists and is correctly formatted

def path_validate( path ):
    # functionality to be added
    return path

def scrape_to( str, dest ):
    dest = path_validate( dest )
    site = urlopen( str )
    site_content = site.read( )
    full_path = dest + str.replace( '/', '.' ) + '.txt'
    site_file = open( full_path, 'w' )
    site_file.write( site_content )
    site_file.close( )
    return
