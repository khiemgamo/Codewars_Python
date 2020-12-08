'''
Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 >> [5,4,3,2,1]
'''

#solution:
def reverse_seq(n):
    rev = []
    for i in range(1,n+1):
        rev.append(n+1-i)
    return rev

#solution 2:
def reverse_seq(n):
    return list(range(n, 0, -1))
