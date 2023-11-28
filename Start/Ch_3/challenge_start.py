# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for comprehensions

import string
import pprint


test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

#Requirements:
#Length of string
#Number of digit characters
#Number of punctuation characters
#string containing all unique letters in the string
#Length of that string

# YOUR CODE HERE



# print the data
str_data = {
    #Get length of string
    "Length: " : len(test_str),
    #Count number of digits
    "Digits " : len([x for x in test_str if x.isdigit()]),
    #Count number of punctuation
    "Punctuation: " : len([x for x in test_str if x in string.punctuation]),
    #Create set of letters
    "Unique Letters: " : (un_str :={x for x in test_str if x.isalpha()}),
    #Get length of the set
    "Unique Count: " : len(un_str)
}
pprint.pp(str_data)
