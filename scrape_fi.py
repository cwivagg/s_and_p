import sys
sys.path.append('/Users/cwivagg/Documents/insight/un_project/web_scraping')

import numpy as np
import pandas as pd
import scraper as s

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
print constituents['site_list'].values[-1]

scraper = s.scraper(constituents['site_list'].values.tolist())
scraper.scrape_all(dest='./stored_websites/',delay=3)
