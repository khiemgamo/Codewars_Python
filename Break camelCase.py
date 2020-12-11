'''
[+]Complete the solution so that the function will break up camel casing, using a space between words.

[+]Example:
solution("camelCasing")  ==  "camel Casing"
'''

#solution:
def solution(s):
    sep = []
    final = ""
    for i in range(len(s)):
        if s[i].isupper():
            sep.append(i)
        else: 
            continue
    final += s[:sep[0]]
    for i in range(len(sep)):
        try:
            final += " " + s[sep[i]:sep[i+1]]
        except:
            final += " " + s[sep[i]:len(s)]
    return final

#solution 2:
def solution(s):
    final = ""
    for char in s:
        if char.isupper():
            final += " " + char
        else:
            final += char
    return final
