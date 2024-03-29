#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
print(configfile.read())

## close file
configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

## Iterate through configlist
for x in configlist:
    print(x)
## Always close your file
configfile.close()

## Iterate through configlist
for x in configlist:
    print(x.strip())   # by default, print() ends in a newline
                       # by passsing end="" print will not "add a second"
                       # newline character
                       #.strip() Strips off beginning and ending white soace
