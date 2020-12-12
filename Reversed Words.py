'''
[+]Complete the solution so that it reverses all of the words within the string passed in.

[+]Example:
==> reverseWords("The greatest victory is that which requires no battle")
should return "battle no requires which that is victory greatest The"
'''

#solution:
def reverseWords(s):
    rev = []
    for i in range(len(s.split())-1,-1,-1):
        rev.append((s.split())[i])
    return " ".join(rev)
