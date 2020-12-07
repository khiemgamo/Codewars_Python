'''
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages
'''

#this solution cause timed out, still optimizing
#solution:
def is_square(n):
    count = 0
    if n < 0:
        return False
    else:
        for i in range(n+1):
            if i * i == n:
                count += 1
        if count < 1:
            return False
        else:
            return True
