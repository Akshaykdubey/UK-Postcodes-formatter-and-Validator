######################################################################
# @Description: Program to print series of numbers in the below format
#               prints the numbers from 1 to 100. But for multiples of 
#               three print “Three” instead of the number and for the 
#               multiples of five print “Five”. For numbers which are 
#               multiples of both three and five print “ThreeFive”.
#               Example:
#               1
#               2
#               Three
#               4
#               Five
#               Three
#               7
#               8
#               Three
#               Five
#               11
#               Three
#               13
#               14
#               ThreeFive
#               ...
#               98
#               Three
#               Five
# @author: Akshay Dubey
######################################################################


def print_number():
    num = 101
    for i in range(1, num):
        # Printing ThreeFive if number is divisible by 3 and 5 both
        if i % 3 == 0 and i % 5 == 0:
            print("ThreeFive")
            
        # Printing Three if number is divisible by 3
        elif i % 3 == 0:
            print("Three")
            
        # Printing five if number is divisible by 5
        elif i % 5 == 0:
            print("Five")
        # Simply print number if none of the above conditions are met
        else:
            print(i)


print_number()
