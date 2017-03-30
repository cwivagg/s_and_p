from os import listdir
from lxml import etree
    
class site_parser:

    def __init__( self ):
        self.to = './'
        self.fro = './'
        self.elements = []
        self.element_format = None
        self.results = []

    def set_targets( self, directory ):
        self.fro = directory

    def set_destination( self, file ):
        self.to = file

    def add_element( self, expr ):
    	self.elements.append( expr )
    
    def format_elements( self, format ):
        self.element_format = format
        for column in format:
            self.results.append( [] )

    # default behavior is
    #    left fill for missing entries;
    #    right fill with whitespace
    #    alternatives to be added later
    def add_to_result_table( self, entry, column=None ):
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
            if col_num > column:
                if len(self.results[col_num]) < \
                      len(self.results[column])-1:
                    self.results[col_num].append('')

    def print_table( self ):
        my_file = open( self.to, 'w' )
        table = self.results
        end_col = len( table )-1
        for row in range(len(table[end_col])):
            for column in range(len(table)):
                my_file.write( table[column][row] )
                my_file.write( ',' if column!=end_col else '\n' )
        my_file.close( )
        print len(table[0]),len(table[2]),table[0][327]

    def parse( self ):
        for file in listdir(self.fro):
            contents = open( self.fro+file, 'r' )
            tree = etree.parse( contents, etree.HTMLParser( ) )
            root = tree.getroot( )
            for ele in self.element_format:
                for result in root.xpath( self.elements[ele] ):
                    #print result
                    result = result.encode( 'ascii', 'ignore' ).strip()
                    self.add_to_result_table( result, ele )
            contents.close( )
        print self.results
        self.print_table( )