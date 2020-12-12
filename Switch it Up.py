'''
[+]When provided with a number between 0-9, return it in words.

[+]Example:
Input :: 1
Output :: "One"
'''

#solution:
def switch_it_up(number):
    numb = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    return numb[number]
