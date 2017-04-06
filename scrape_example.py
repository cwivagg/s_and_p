"""Download morningstar.com company director listings.

Requires a companion file entitled "constituents.csv" with company ticker
   symbols in a column headed "Symbols".
Requires the directory stored_websites.

This code downloads a series of websites, in this case, a simple set of
data about each of the S and P 500 components from morningstar.com.
The scraper takes two arguments: 1) a directory in which to store the web-
sites, 2) a crawl delay. Because I like to be very respectful and I was
downloading such a small number of websites, I set a very large crawl delay
of 3 s.

"""

import numpy as np
import pandas as pd
from web_scraping import scraper

def main():
    """ Invoke scraper from web_scraping module to download listings."""

    # A list of ticker symbols I found on the Internet. The morningstar URLs for
    # each company are the same except for the symbols, which function as keys.
    constituents = pd.read_csv('constituents.csv')
    ticker_symbols = constituents['Symbol'].values

    prefix = 'http://www.reuters.com/finance/stocks/companyOfficers?symbol='
    suffix = ''
    constituents['prefix'] = prefix
    constituents['suffix'] = suffix

    constituents['site_list'] = constituents[[
                               'prefix',
                               'Symbol',
                               'suffix' ]].apply(lambda x: ''.join(x), axis=1)

    scraper = scraper.Scraper(constituents['site_list'].values.tolist())
    scraper.scrape_all(dest='./stored_websites/', delay=3)

if __name__ == "__main__":
    main()
