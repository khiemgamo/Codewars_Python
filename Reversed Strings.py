'''
[+]Complete the solution so that it reverses the string passed into it.

[+]Example:
'world'  =>  'dlrow'
'''

#solution:
def solution(string):
    rev = ""
    for i in range(len(string)-1,-1,-1):
        rev += string[i]
    return rev

#solution 2:
def solution(string):
    return string[::-1]
