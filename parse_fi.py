import sys
sys.path.append('./web_scraping')

import site_parser as p

# selecting web elements we desire
#  1. company
#  2. company officers
#  3. company officers' positions

ele = []
ele.append( './/h1/text()' )
ele.append( './/h2/a/text()' )
ele.append( './/tbody/tr/td[4]/text()' )

parser = p.site_parser()
parser.set_destination('./parsed_officers')
parser.set_targets('./stored_websites/')
for element in ele:
	parser.add_element(element)
parser.format_elements( (0,1,2) )
parser.parse()