##################################################################
# @Description: This unittest is to test the library 'UKPostcodes'
#               for formatting and validating UK Postcodes.
# @Testcases:
#            1) test_format_postcode1 : 'Unit test to test the formatting the Postcode'
#            2) test_format_postcode2 : 'Unit test to test the formatting the Postcode.
#                                        Checks special character and throws an exception.'
#            3) test_format_postcode3 : 'Unit test to test formatting of the Postcode
#                                        Checks for length of Postcode and throws an exception
#                                        if the the length doesn't lie between 6 and 8'
#            4) test_validate_component_postcode1 : 'Unit test to validate the different
#                                        components of the Postcode. Positive case
#                                        Double Digit District'
#            5) test_validate_component_postcode2 : 'Unit test to validate the different
#                                        components of the Postcode. Positive case
#                                        Single Digit District'
#            6) test_validate_postcode1 : 'Unit test for validating the Postcode. Positive case'
#            7) test_validate_postcode2 : 'Unit test for validating the Postcode. Negative case
#                                          The letters QVX are not used in the first position'
#            8) test_validate_postcode3 : 'Unit test for validating the Postcode. Negative case
#                                          Only letters to appear in the third position are ABCDEFGHJKPSTUW'
#            9) test_validate_postcode4 : 'Unit test for validating the Postcode. Negative case
#                                          Only letters to appear in the fourth position are ABEHMNPRVWXY'
#            10) test_validate_postcode5 : 'Unit test for validating the Postcode. Negative case
#                                          The letters IJZ are not used in the second position'
#            11) test_validate_postcode6 : 'Unit test for validating the Postcode. Negative case
#                                          The final two letters do not use the letters CIKMOV'
# @author: Akshay Dubey
##################################################################

import unittest
from UKPostcodes import PostCodes


class TestPostCodes(unittest.TestCase):

    def test_format_postcode1(self):
        """ Unit test to test formatting of the Postcode
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
            print("Expected an exception.\n"
                  "Postcode contains special character.\n"
                  "Test2: Successful")

    def test_format_postcode3(self):
        """ Unit test to test formatting of the Postcode
            Checks for length of Postcode and throws an exception
            if the the length doesn't lie between 6 and 8
        """
        postcode_inst = PostCodes(10)
        try:
            postcode_inst.format_postcode('PO167')
        except TypeError:
            print("Expected an exception.\n"
                  "Length of the Postcode should be between 6 and 8.\n"
                  "Test3: Successful")

    def test_validate_component_postcode1(self):
        """ Unit test to validate the different
            components of the Postcode
            Positive case Double Digit District
        """
        postcode_inst = PostCodes(10)
        num = postcode_inst.validate_postcode_components('PO167GZ')
        assert num.postcode_area == 'PO' and num.postcode_district == '16'\
               and num.postcode_sector == '7' and num.postcode_unit == 'GZ'
        print("Postcode Area: " + num.postcode_area + "\nPostcode district: " + num.postcode_district + \
              "\nPostcode sector: " + num.postcode_sector + "\nPostcode Unit: " + num.postcode_unit + \
              "\nTest4: Successful")

    def test_validate_component_postcode2(self):
        """ Unit test to validate the different
            components of the Postcode
            Negative case
        """
        postcode_inst = PostCodes(10)
        num = postcode_inst.validate_postcode_components('PO167GZ')
        assert num.postcode_area == 'PO' and num.postcode_district == '16'\
               and num.postcode_sector == '7' and num.postcode_unit == 'GZ'
        print("Postcode Area: " + num.postcode_area + "\nPostcode district: " + num.postcode_district + \
              "\nPostcode sector: " + num.postcode_sector + "\nPostcode Unit: " + num.postcode_unit + \
              "\nTest5: Successful")

    def test_validate_postcode1(self):
        """ Unit test for validating of the Postcode
            Positive case
        """
        postcode_inst = PostCodes(10)

        num = postcode_inst.validate_postcode('PO167GZ')
        assert num == True
        print('Test6: Successful')

    def test_validate_postcode2(self):
        """ Unit test for validating of the Postcode
            Negative case
        """
        postcode_inst = PostCodes(10)

        # The letters QVX are not used in the first position
        num = postcode_inst.validate_postcode('VC1A 1BB')
        assert num == False
        print('Test7: Successful')

    def test_validate_postcode3(self):
        """ Unit test for validating of the Postcode
            Negative case
        """
        postcode_inst = PostCodes(10)

        # Only letters to appear in the third position are ABCDEFGHJKPSTUW
        num = postcode_inst.validate_postcode('A9X 0AX')
        assert num == False
        print('Test8: Successful')

    def test_validate_postcode4(self):
        """ Unit test for validating of the Postcode
            Negative case
        """
        postcode_inst = PostCodes(10)

        # Only letters to appear in the fourth position are ABEHMNPRVWXY
        num = postcode_inst.validate_postcode('AA9C 0AX')
        assert num == False
        print('Test9: Successful')

    def test_validate_postcode5(self):
        """ Unit test for validating of the Postcode
            Negative case
        """
        postcode_inst = PostCodes(10)

        # The letters IJZ are not used in the second position
        num = postcode_inst.validate_postcode('VI1A 1BB')
        assert num == False
        print('Test10: Successful')

    def test_validate_postcode6(self):
        """ Unit test for validating of the Postcode
            Negative case
        """
        postcode_inst = PostCodes(10)

        # The final two letters do not use the letters CIKMOV
        num = postcode_inst.validate_postcode('PO167GV')
        assert num == False
        print('Test11: Successful')


if __name__ == '__main__':
    unittest.main()
