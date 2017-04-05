# Overview
This repository contains python code allowing the user to 
  1) scrape information about every company in the S and P 500 from morningstar.com,
  2) parse and clean this data
  3) map and analyze this data to identify important companies and persons.

These functionalities are encoded in the scripts scrape_fi.py, parse_fi,py, and network_analysis.ipynb; accompanying helper functions are in the directory web_scraping.
# To Use
## 1) Git Clone
```
git clone https://github.com/cwivagg/s_and_p
```
## 2) Terminal
First, scrape_example.py downloads websites containing the boards of directors and company officers for each company in the S&P 500 stock index.
```
$ mkdir stored_websites
$ python scrape_example.py
```
Next, parse_example.py extracts the individual companies, officers, and position titles from the stored HTML files and formats them in a tab-delimited text file.
```
$ python parse_example.py
```
Finally, for ease of visualization and easy modifiability, the analysis is conducted in a Jupyter notebook.
```
$ jupyter notebook
```
More information on installing and using Jupyter notebooks can be found [here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest).
