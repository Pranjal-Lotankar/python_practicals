'''A pangram is a sentence that contains all the letters of the English alphabet at
least once, for example: The quick brown fox jumps over the lazy dog. Your task
here is to write a function to check a sentence to see if it is a pangram or not.'''

from string import ascii_lowercase as asc_lower

def check(s):
    return set(asc_lower) - set(s.lower()) == set([])
strng = input("Enter string:")

if(check(strng)==True):
    print("The string is a pangram")
else:
    print("The string isn't a pangram")
