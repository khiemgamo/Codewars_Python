'''
[+]The main idea is to count all the occurring characters in a string. 

[+]For example,
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

[+]What if the string is empty? Then the result should be empty object literal, {}
'''

#solution:
def count(string):
    data = {}
    for char in string:
        data[char] = 0
        data[char] += string.count(char)
    return data
