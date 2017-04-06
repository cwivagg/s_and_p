"""Site parsers: these objects parse the contents of websites.

Classes:
site_parser -- should be used as the default option
"""

from os import listdir
from lxml import etree

class SiteParser(object):
    """Systematically extracts specific html elements from a document.

    site_parser methods:
    set_targets -- directory of documents to be parsed
    set_destination -- location and name of the output file
    add_element -- specify an html element to extract
    format_elements -- specify an output format
    parse - activates fully specified parser
    """

    def __init__(self):
        """Initialize a parser.
        """
        self.outdoc = './temp'
        self.fro = self.set_targets('./')
        self.elements = []
        self.element_format = None
        self.results = []

    def set_targets(self, directory):
        """Set the pages to be parsed.

        Currently these should be passed in the form of a directory containing
        only the files to be parsed.
        """
        self.fro = [directory+file for file in listdir(directory) \
            if file[0] != '.']

    def set_destination(self, file):
        """Set the location of the output file the parser produces.

        Currently this file will be a tab-delimited table.
        """
        self.outdoc = file

    def add_element(self, expr):
        """Adds an element to the list of elements to parse for each document.

        Elements should be formulated as XPath strings.
        """
        self.elements.append(expr)

    def format_elements(self, format):
        """Specifies the column order in which to output elements.

        Column order is a tuple with a number of elements equal to the number
        added by add_elements. If add_elements is invoked again, a new format
        must be specified.
        """
        self.element_format = format
        for column in format:
            self.results.append([])

    def add_to_result_table(self, entry, column=None):
        """PRIVATE: adds a parsed element to an internal buffer.

        UNDER DEVELOPMENT
        Current behavior is not well-tested for missing entries.
        Left fill for missing entries occurs.
        Right fill with whitespace for missing entries occurs.
        Ideally these fill responses will eventually be customizable.
        """
        if not self.element_format:
            results.append(entry)
            return
        for col_num in range(len(self.results)):
            if col_num < column:
                if len(self.results[col_num]) <= \
                      len(self.results[column]):
                    self.results[col_num].append(self.results[col_num][-1])
            if col_num == column:
                self.results[col_num].append(entry)

    def make_rows_nice(self):
        """PRIVATE: Makes sure table is constructed properly in self.parse
        """
        max_lens = [len(col) for col in self.results]
        max_len = max(max_lens)
        for col in self.results:
            while max_len > len(col):
                col.append('')

    def print_table(self, delimiter='\t'):
        """PRIVATE
        """
        my_file = open(self.outdoc, 'w')
        table = self.results
        end_col = len(table)-1
        for row in range(len(table[end_col])):
            for column, _ in enumerate(table):
                my_file.write(table[column][row])
                my_file.write(delimiter if column != end_col else '\n')
        my_file.close()

    def parse(self):
        """PRIVATE
        """
        for file in self.fro:
            contents = open(file, 'r')
            tree = etree.parse(contents, etree.HTMLParser())
            root = tree.getroot()
            for ele in self.element_format:
                results = root.xpath(self.elements[ele])
                if not results:
                    continue
                for result in results:
                    str_result = result.encode('ascii', 'ignore').strip()
                    self.add_to_result_table(str_result, ele)
                self.make_rows_nice()
            contents.close()
        self.print_table()
