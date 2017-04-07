"""Invoke src.parser to process morningstar.com downloads.

This code takes the raw html of a website, invokes my parser class, and
extracts specified text elements. The parser operates on a directory of
downloaded websites and outputs a single file containing the tabulated
extracted information.

parse_example.py currently expects the downloaded websites to be lists the
Morningstar company officer listings, stored in a directory called
stored_websites.

"""

import sys
from src import site_parser

def main():
    """Invoke src.parser as described above."""

    # Select web elements we desire.
    #  1. company
    #  2. company officers
    #  3. company officers' positions
    ele = []
    ele.append('.//h1/text()')
    ele.append('.//h2/a/text()')
    ele.append('.//tbody/tr/td[4]/text()')

    parser = site_parser.SiteParser()
    parser.set_destination('./parsed_officers')
    parser.set_targets('./stored_websites/')
    for element in ele:
        parser.add_element(element)

    # Currently we can store extracted data as a table or as a list.
    #   For a list, leave the argument blank.
    #   For a table, specify the column order of the elements specified above.
    parser.format_elements((0, 1, 2))

    parser.parse()

if __name__ == "__main__":
    main()
