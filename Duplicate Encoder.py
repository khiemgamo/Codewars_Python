'''
[+]The goal of this exercise is to convert a string to a new string
where each character in the new string is "(" if that character appears only once in the original string,
or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

[+]Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
'''

#solution:
def duplicate_encode(word):
    encoded = ""
    for char in word.lower():
        if (word.lower()).count(char) > 1:
            encoded += ")"
        else:
            encoded += "("
    return encoded
