###########################################################################
# @description: This library is for formatting and validating UK
#               Postcodes.
# @functions:
#            1) format_postcode(self, postcode_value)
#               @arguments:
#               -> postcode_value: Value for the Postcode to be formatted
#               @usage:
#                     Step1: Create an instance of the class
#                     inst = PostCodes()
#                     Step 2: Call the method format_postcode
#                     inst.format_postcode('PO167GZ')
#               @returns: Formatted Postcode
#               @output: PO16 7GZ
#            2) validate_postcode(self, postcode_value)
#               @arguments:
#               -> postcode_value: Value for the Postcode to be validated
#               @usage:
#                     Step1: Create an instance of the class
#                     inst = PostCodes()
#                     Step 2: Call the method validate_postcode
#                     inst.validate_postcode('PO167GZ')
#               @returns: True if the Postcode is validated else False
#               @output: True/False
# @author: Akshay Dubey
###########################################################################


import re

postcode_regex = '(GIR 0A{2})|[A-PR-UWYZ](([A-HK-Y]?\d\d?)|(\d[A-HJKPSTUW])|'\
    '([A-HK-Y]\d[ABEHMNPRV-Y]))[ ]?\d[ABD-HJLNP-UW-Z]{2}'
code = re.compile('^{}$'.format(postcode_regex), re.I)


class PostCodes:

    def __init__(self, input_code, formatted_postcode = ''):
        self.input_code = input_code
        self.formatted_postcode = formatted_postcode

    def format_postcode(self, postcode_value):
        """ Function to format the Postcode
            returns the formatted Postcode
        """

        # Replacing all the spaces from the input Postcode
        value = postcode_value.replace(" ", "")

        # Throw an exception if the length of the Postcode is less than 6 or greater than 8 characters.
        if len(value) < 5 or len(value) > 7:
            raise TypeError('Error: The length of the postcode should be from 6 to 8 characters only.')

        # Throw an exception if there is any special characters in the Postcode
        if not value.isalnum():
            raise TypeError('Error: No special characters are allowed in the Postcode.')

        # Converting into uppercase
        code = value.upper()
        # Extracting outward code from the input Postcode, i.e., stripping last 3 characters
        out_code = code[:-3].strip()
        # Extracting inward code from the input Postcode, i.e., stripping all characters except last 3
        inw_code = code[-3:].strip()

        return out_code + ' ' + inw_code

    def validate_postcode(self, postcode_value):
        """ Function to validate the Postcode
            return True if the Postcode is valid
            else return False
        """

        # Formatting the Postcode before validating.
        formatted_postcode = self.format_postcode(postcode_value)
        self.formatted_postcode = formatted_postcode
        # Validating the Postcode
        if re.match(postcode_regex, formatted_postcode):
            return True
        else:
            return False

    def validate_postcode_components(self, postcode_value):
        """ Function to validate the Postcode and return
            the different components of Postcode, i.e.,
            Postcode Area, Postcode District,Postcode Sector,
            Postcode Unit
            return True if the Postcode is valid
            else return False
        """



