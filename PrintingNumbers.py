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
        if i % 3 == 0 and i % 5 == 0:
            print("ThreeFive")
        elif i % 3 == 0:
            print("Three")
        elif i % 5 == 0:
            print("Five")
        else:
            print(i)


print_number()
