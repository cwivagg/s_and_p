# Overview
The purpose of this repository is to enable visualization of the links between large companies in the United States. Inspired by the brilliant [work](https://kieranhealy.org/blog/archives/2013/06/09/using-metadata-to-find-paul-revere/) of Kieran Healy, I wished to see whether extremely simple information about people, such as which directors sit on which boards together, could tell us anything about the structure of corporate America.

This project is presently under construction. It is designed to be extensible and modifiable. The scraping and parsing module is a light wrapper for Python's urllib2 and lxml libraries; my hope was to create a small module of my own that would lessen the work involved in scraping tables of data from the Internet, a task that has been common to several recent projects I have undertaken.
# To Use
## 1) Git Clone
Before executing the elements of the repository it is necessary to clone it. The simplest way is to directly clone the repository from the command line. If you have not done so before, full instructions for installing git can be found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
```
git clone https://github.com/cwivagg/s_and_p
```
If you do not wish to use the command line, use the buttons at the top right of the page.
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
Once the Jupyter app has loaded, select the network_analysis notebook.
