# python website parser
#   This code takes the raw html of a website, invokes my parser class, and
#   extracts specified text elements. The parser operates on a directory of
#   downloaded websites and outputs a single file containing the tabulated
#   extracted information.

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
parser.set_targets('./stored_websites2/')
for element in ele:
	parser.add_element(element)

# currently we can store extracted data as a table or as a list
#   for a list, leave the argument blank;
#   for a table, specify the column order of the elements specified above
parser.format_elements( (0,1,2) )

parser.parse()
