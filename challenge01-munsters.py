#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Review of Lists and Dictionaries"""

# define a short data set (in real world, we want to read this from a file or API)
munsters = {'endDate': 1966, 'startDate': 1964,\
        'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}   # {} creates dict

# Your solution goes below this line
# ----------------------------------

# Display the value mapped to names
print('The names of the munsters are', munsters ['names'])

# Display the value mapped to enddate
print('The EndDate for the munsters is', munsters ['endDate'])


#Display the value mapped to startDate
print('The StartDate for the Munsters is', munsters ['startDate'])


#Add a new key, episodes mapped to a vlaue of 70
munsters['episodes'] = int(70)
print('A total of' , munsters['episodes'], 'episodes were created')

user_imput = input('Did you ever watch The Munsters ?')
print('Your answer was', user_imput )



