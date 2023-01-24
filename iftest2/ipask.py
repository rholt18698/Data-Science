#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - testing if strings test true"""

ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true

if ipchk:
    print("looks like the ip address was set: " + ipchk)  # indented under if

else:  # if data is NOT provided
    print("You did not provide any input")  #indented under else

