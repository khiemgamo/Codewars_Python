'''
[+]Given an array of integers of any length, return an array that has 1 added to the value represented by the array.
[.]the array can't be empty
[.]only non-negative, single digit integers are allowed
[.]Return None (or your language's equivalent) for invalid inputs.

[+]Examples
For example,
the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].
[4, 3, 2, 5] would return [4, 3, 2, 6]
'''

#solution:
def up_array(arr):
    print(arr)
    num = ""
    if arr == []:
        return None
    else:
        for i in range(len(arr)):
            if arr[i] < 0:
                return None
                break
            elif arr[i] > 9:
                return None
                break
            else:    
                num += str(arr[i])
        return [int(i) for i in str(int(num) + 1)]
