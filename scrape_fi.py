# python web scraper
#   This code downloads a series of websites, in this case, a simple set of
#   data about each of the S and P 500 components from morningstar.com.
#   The scraper takes two arguments: 1) a directory in which to store the web-
#   sites, 2) a crawl delay. Because I like to be very respectful and I was
#   downloading such a small number of websites, I set a very large crawl delay
#   of 3 s.

import sys
sys.path.append('./web_scraping')

import numpy as np
import pandas as pd
import scraper as s

# A list of ticker symbols I found on the Internet. The morningstar URLs for
#   each company are identical except for the ticker symbols, which function as
#   keys.
constituents = pd.read_csv('sandp_constituents.csv')
ticker_symbols = constituents['Symbol'].values

prefix = 'http://www.reuters.com/finance/stocks/companyOfficers?symbol='
suffix = ''
constituents['prefix'] = prefix
constituents['suffix'] = suffix

constituents['site_list'] = constituents[[
                           'prefix', \
                           'Symbol', \
                           'suffix' ]].apply(lambda x: ''.join(x), axis=1)

scraper = s.scraper(constituents['site_list'].values.tolist())
scraper.scrape_all(dest='./stored_websites/',delay=3)
