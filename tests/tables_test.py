"""Test reading, parsing, and printing of a standard financial site.

Members:
OfflineTests -- test parser only
OnlineTests -- include scraper downloading
"""

import unittest
import joblib

class OfflineTests(unittest.TestCase):

    """Test reading, parsing, and printing of a financial site on disk.

    Methods:
    test_read -- tests ability to parse stored file
    test_parse -- tests ability to store elements in internal table
    test_print -- tests ability to print table correctly
    """

    def test_read(self):
    """Tests continuity of parsing functionality."""
        pass

    def test_parse(self):
    """Compares extracted elements of read to their known values."""
        pass

    def test_print(self):
    """Compares a small table to its known value after parsing."""
        pass

class OnlineTests(OfflineTests):

    """Offline tests with the added step of requesting the website.

    Multiple tests are recommended against the possibility that data has
    changed, although this battery of tests is selected from websites
    thought to be unlikely to change. Individual methods can be ommitted
    or fixed if the assumption turns out to be false.
    Methods:
    test_bartleby -- tests bartleby.com
    test_mit -- tests the MIT classics archive
    """

    def test_bartleby(self):
    """Test a Bartleby.com page against its memory representation."""
    pass

    def test_mit(self):
    """Test a page from the MIT Archive against its memory representation."""
    pass
