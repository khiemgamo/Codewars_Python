'''
[+]Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

[+]Examples:
solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
'''

#solution:
def solution(s):
    word = []
    if len(s) % 2 == 1:
        s += "_"
    for i in range(1,len(s),2):
        word.append(s[i-1:i+1])
    return word
