'''
Write a function reverse which reverses a list (or in clojure's case, any list-like data structure)

(the dedicated builtin(s) functionalities are deactivated)
'''

#solution:
def reverse(lst):
    empty_list = list()
    for i in range(len(lst)):
        order = len(lst)- 1 - i
        empty_list.append(lst[order])
    return empty_list
