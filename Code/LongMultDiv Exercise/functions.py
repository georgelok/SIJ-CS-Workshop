from Imports.Classes import Digit, Number
'''
Wrapper Functions for <Insert Exercise Name Here>

Use these functions to 
'''

'''

'''
def generateNumberFromString(value) :
  '''
  Generates a number object from a string.
  '''
  try :
    return Number(value)
  except TypeError :
    raise TypeError("You did not pass in a valid integer.")