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
#            2) validate_postcode_components(self, postcode_value)
#               @arguments:
#               -> postcode_value: Value for the Postcode to be validated
#               @usage:
#                     Step1: Create an instance of the class
#                     inst = PostCodes()
#                     Step 2: Call the method validate_postcode_components
#                     inst.validate_postcode_components('PO167GZ')
#               @returns: self object containing components of Postcode
# @author: Akshay Dubey
###########################################################################

# import libraries
import re

POSTCODE_REGEX = '(GIR 0A{2})|[A-PR-UWYZ](([A-HK-Y]?\d\d?)|(\d[A-HJKPSTUW])|'\
    '([A-HK-Y]\d[ABEHMNPRV-Y]))[ ]?\d[ABD-HJLNP-UW-Z]{2}'
CODE = re.compile('^{}$'.format(POSTCODE_REGEX), re.I)

# Areas with only single-digit districts
SINGLE_DIGIT_DISTRICT = ['BR', 'FY', 'HA', 'HD', 'HG', 'HR', 'HS', 'HX', 'JE', 'LD', 'SM', 'SR', 'WC', 'WN', 'ZE']

# Areas with only double-digit districts
DOUBLE_DIGIT_DISTRICT = ['AB', 'LL', 'SO']

# Areas with a district '0' (zero)
AREA_DISTRICT_ZERO = ['BL', 'BS', 'CM', 'CR', 'FY', 'HA', 'PR', 'SL', 'SS']

# The following central London single-digit districts have been further divided by inserting a letter after the digit
# and before the space: EC1–EC4 (but not EC50), SW1, W1, WC1, WC2
SPECIAL_SINGLE_DIGIT_DISTRICT = ['EC1', 'EC2', 'EC3' 'EC4', 'SW1', 'W1', 'WC1', 'WC2']

# although WC is always subdivided by a further letter, e.g. WC1A
# BS is the only area to have both a district 0 and a district 10
# part of E1 (E1W), N1 (N1C and N1P), NW1 (NW1W) and SE1 (SE1P)
SPECIAL_OUTWARD_CODE = ['WC1A', 'BS10', 'E1W', 'N1C', 'N1P', 'NW1W', 'SE1P']

# Invalid outward code of the Postcode
INVALID_OUT_CODE = ['E1', 'N1', 'NW1', 'SE1', 'EC50']

class PostCodes:

    def __init__(self, input_code,
                 formatted_postcode='',
                 outward_code='',
                 inward_code='',
                 postcode_area='',
                 postcode_district='',
                 postcode_unit='',
                 postcode_sector=''):
        self.input_code = input_code
        self.formatted_postcode = formatted_postcode
        self.outward_code = outward_code
        self.inward_code = inward_code
        self.postcode_area = postcode_area
        self.postcode_district = postcode_district
        self.postcode_unit = postcode_unit
        self.postcode_sector = postcode_sector

    def format_postcode(self, postcode_value):
        """ Function to format the Postcode
            returns the formatted Postcode
        """

        # Replacing all the spaces from the input Postcode
        value = postcode_value.replace(" ", "")

        # Throw an exception if the length of the Postcode is less than 6 or greater than 8 characters.
        if len(value) < 5 or len(value) > 7:
            raise TypeError('ERROR: The length of the postcode should be from 6 to 8 characters only.')

        # Throw an exception if there is any special characters in the Postcode
        if not value.isalnum():
            raise TypeError('ERROR: No special characters are allowed in the Postcode.')

        # Converting into uppercase
        code_upper = value.upper()
        # Extracting outward code from the input Postcode, i.e., stripping last 3 characters
        out_code = code_upper[:-3].strip()
        # Extracting inward code from the input Postcode, i.e., stripping all characters except last 3
        inw_code = code_upper[-3:].strip()
        self.outward_code = out_code
        self.inward_code = inw_code
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
        if re.match(CODE, formatted_postcode):
            return True
        else:
            return False

    def validate_postcode_components(self, postcode_value):
        """ Function to validate the Postcode and return
            the different components of Postcode, i.e.,
            Postcode Area, Postcode District,Postcode Sector,
            Postcode Unit
            return self object containing different component
            of the Postcode
        """

        validate = self.validate_postcode(postcode_value)

        if validate:

            # Find the index of the first digit in the outward code
            index_digit = re.search("\d", self.outward_code).start()

            # Fetching Postcode area from the outward code
            self.postcode_area = self.outward_code[:index_digit]

            # Fetching Postcode district from the outward code
            self.postcode_district = self.outward_code[index_digit:]

            # Checking conditions on postcode_area
            if self.outward_code.startswith(tuple(INVALID_OUT_CODE)):
                raise TypeError("ERROR: Invalid Postcode")
            elif not (self.outward_code in SPECIAL_OUTWARD_CODE):
                if self.outward_code.startswith(tuple(SPECIAL_SINGLE_DIGIT_DISTRICT)):
                    if not self.postcode_district[-1:].isalpha():
                        raise TypeError("ERROR: Invalid Postcode")
                elif self.postcode_area in SINGLE_DIGIT_DISTRICT:
                    if len(self.postcode_district) != 1 or not (self.postcode_district.isdigit()):
                        raise TypeError("ERROR: Invalid Postcode")
                elif self.postcode_area in DOUBLE_DIGIT_DISTRICT:
                    if len(self.postcode_district) != 2 or not (self.postcode_district.isdigit()):
                        raise TypeError("ERROR: Invalid Postcode")
                elif self.postcode_area in AREA_DISTRICT_ZERO:
                    if self.postcode_district != '0':
                        raise TypeError("ERROR: Invalid Postcode")

            self.postcode_sector = self.inward_code[:1].strip()
            self.postcode_unit = self.inward_code[1:].strip()

        return self
