import unittest
from functions.regex_functions import *

class CustomerTestCase(unittest.TestCase):
    """Tests the functions in the regex_functions.py file"""

    def test_CC_success(self):
        """Here is a bunch of CCs I think should work"""
        valid_CCs_to_test = ["40041257849597", "46474758960596", "492922 277541 3883", "4556799984114","4485 730 49 2187","4564 567 71 8540","492 97100 29124 678"]

        for number in valid_CCs_to_test:
            self.assertTrue(isValidCC(number))

    def test_CC_failure(self):
        """Here is a bunch of CCs I think should not work"""
        invalid_CCs_to_test = ["", " 12100948$56456849", "credit card # is 402939454323", "asdasdasdasd123123123123123123 ", " 4029183//574844"]

        for number in invalid_CCs_to_test:
            self.assertFalse(isValidCC(number))

    def test_coord_success(self):
        """Here is a bunch of coords I think should work"""
        valid_coords_to_test = ["-24.97415, -94.2243", "70.37374, 88.5683", "-51.85958, 106.62751", "-15.94064, 169.44626", "-3.19772, -83,1604"]

        for coord in valid_coords_to_test:
            self.assertTrue(isValidCoord(coord))

    def test_coord_failure(self):
        """Here is a bunch of coords I think should not work"""
        invalid_coords_to_test = ["", "	-3.19772, -83.16040505958576", "	-31234.19772, -83.1604 ", "0947", "coords are -51.85958, 106.6275112","8070,505059,574645.57684"]

        for coord in invalid_coords_to_test:
            self.assertFalse(isValidCoord(coord))
        
    def test_dollar_success(self):
        """Here are some dollar amounts I think should succeed"""
        valid_dollars_to_test = ["$ 5,687", "$ 5,978", "$ 4,057", "$ 3,798","$ 7.980","$ 7.364"]

        for dollar in valid_dollars_to_test:
            self.assertTrue(isValidDollar(dollar))
    
    def test_dollar_failure(self):
        """Here are some dollar amounts I think should fail"""
        invalid_dollars_to_test = ["", "$5687", " $59,803", "$  5867","5986","$ 5986.00"]

        for dollar in invalid_dollars_to_test:
            self.assertFalse(isValidDollar(dollar))
