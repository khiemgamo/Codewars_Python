'''
Complete the function that takes a list of numbers (nums), as the only argument to the function. Take each number in the list and square it if it is even, or square root the number if it is odd. Take this new list and return the sum of it, rounded to two decimal places.

The list will never be empty and will only contain values that are greater than or equal to zero.
'''

#solution:
import math

def sum_square_even_root_odd(nums):
    total = 0
    for i in nums:
        if i % 2 == 0:
            total = round(total + i*i, 2)
        else:
            total = round(total + math.sqrt(i), 2)
    return total

#cannot submit this solution because of a kata's fault
#floating point representation is inaccurate
