import csv
import unittest
from panda import year

class YearTestCase(unittest.TestCase):
    """Tests for `panda.py`."""

    def testyear(self):
        """Is year in there?"""
        self.assertTrue(year('2009'))

if __name__ == '__main__':
    unittest.main()
