'''
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.
'''

#solution:
def quarter_of(month):
    first = [1,2,3]
    second = [4,5,6]
    third = [7,8,9]
    fourth = [10,11,12]
    
    if month in first:
        return 1
    if month in second:
        return 2
    if month in third:
        return 3
    if month in fourth:
        return 4
      
#solution 2:
def quarter_of(month):
  if month in range(1,4):
    return 1
  elif month in range(4,7):
    return 2
  elif month in range(7,10):
    return 3
  else:
    return 4
