# Unit tests and Test Cases
# The module unittest from Python standard library provides tools for testing your code
# A unit test verifies that one specific aspect of a function's behavior is correct.
# A test case is a collection of unit tests that together prove that a function behaves as it's supposed to, within the full range of situations you expect it to handle
# A good test case considers all the possible kinds of input a function could recive and includes tests to represent each of these situations

# To write a test case for function, import the unittest module and the function you want to test
import unittest
from unit_11_example_1_w import get_formatted_name

# Then create a class that inherits from unittest.TestCase
# Write a series of methods to test different aspects of your function's behavior

# Create a class called NamesTestCase, which contain a series of unit tests for get_formatted_name()
class NamesTestCase(unittest.TestCase):
    """Tests for 'unit_11_example_1_w.py'."""

    def test_first_last_name(self):
        """Do names like 'Jennie Kim' work?"""

        # within this test method, we call the function we want to test and store a return value that we are interested in testing
        formatted_name = get_formatted_name('jennie', 'kim')

        # Assert methods verify that a result you received matches the result you expected to recieve
        # Compare the value in formatted_name to the string 'Jennie Kim'
        self.assertEqual(formatted_name, 'Jennie Kim')

unittest.main()