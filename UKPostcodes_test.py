##################################################################
# @Description: This library is for formatting and validating UK
#               Postcodes.
#
#
#
#
#
#


import unittest
from UKPostcodes import PostCodes


class TestPrintNumbers(unittest.TestCase):

    def test_format_postcode1(self):
        """ Unit test for formatting of the Postcode
            Positive case
        """
        postcode_inst = PostCodes(10)
        num = postcode_inst.format_postcode('PO167GZ')
        assert num == 'PO16 7GZ'
        print("Formatted Postcode: " + num + "\nTest1: Successful")

    def test_format_postcode2(self):
        """ Unit test for formatting of the Postcode
            Checks for special characters in the Postcode and throws an exception
        """
        postcode_inst = PostCodes(10)
        try:
            postcode_inst.format_postcode('PO16 #7GZ')
        except TypeError:
            print("Expected an exception.\n"\
                  "Postcode contains special character.\n"\
                  "Test2: Successful")

    def test_validate_component_postcode1(self):
        postcode_inst = PostCodes(10)
        num = postcode_inst.validate_postcode_components('PO167GZ')
        print(num.postcode_area, num.postcode_sector, num.postcode_unit, num.postcode_district)

    def test_validate_postcode1(self):
        """ Unit test for validating of the Postcode
            Positive case
        """
        postcode_inst = PostCodes(10)

        num = postcode_inst.validate_postcode('PO167GZ')
        assert num == True
        print('Test3: Successful')




if __name__ == '__main__':
    unittest.main()
