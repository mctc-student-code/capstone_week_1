import unittest # standard library unit testing framework
from unittest import TestCase

import lawn_quotes # imports the program to test

class QuoteTest(TestCase): # QuoteTest is subclass of TestCase
    """ TestCase: Collection of test
    Each Test is a function, all test function starts their name with test
    Assertion methods are key in unit testing , there are many assertion methods
    """
    
    def test_quote_for_small_lawn_same_day(self):
        actual_quote = lawn_quotes.lawn_quote('small', True) # calls the lawn_quote() function from the program being tested- lawn_quotes.py
        expected_quote = 15
        self.assertEqual(expected_quote, actual_quote) # assertion - heart of unit testing - makes it automatic
    
    def test_quote_for_large_lawn_not_same_day(self):
        actual_quote = lawn_quotes.lawn_quote('large', False) # calls the lawn_quote() function from the program being tested- lawn_quotes.py
        expected_quote = 20
        self.assertEqual(expected_quote, actual_quote)
    
    def test_quote_for_unrecognized_size(self):
        actual_quote = lawn_quotes.lawn_quote('alligator',False) # calls the lawn_quote() function from the program being tested- lawn_quotes.py
        self.assertIsNone(actual_quote)   


if __name__ == '__main__':
    unittest.main() # uses imported module unittest to run the test