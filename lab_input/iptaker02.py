#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - concatenate vs print a series of items"""

def main():
    # collect string input from user\
    user_input = input("Please enter an IPv4 address:")
    
    # collect vendor name
    vendor_name = input("Please enter a vendor name associated with this device:")


    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is: " + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)
    print("You told me the vendor is:", vendor_name)


main()

