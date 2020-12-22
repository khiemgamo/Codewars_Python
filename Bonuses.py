'''
[+]John wants to give a total bonus of $851 to his three employees taking fairly as possible into account their number of days of absence during the period under consideration.
Employee A was absent 18 days, B 15 days, and C 12 days.
The more absences, the lower the bonus ...

[+]How much should each employee receive?
John thinks A should receive $230, B $276, C $345 since [230 * 18 = 276 * 15 = 345 * 12] and [230 + 276 + 345 = 851].

[+]Task:
Given an array arr (numbers of days of absence for each employee) and a number s (total bonus) the function bonus(arr, s) will follow John's way
and return an array of the fair bonuses of all employees in the same order as their numbers of days of absences.

[+]s and all elements of arr are positive integers.

[+]Examples:
bonus([18, 15, 12], 851) -> [230, 276, 345]
bonus([30, 27, 8, 14, 7], 34067) -> [2772, 3080, 10395, 5940, 11880]
'''

#solution:
def bonus(arr, s):
    final = []
    element = 1
    for i in range(1,len(arr)):
        element += arr[0]/arr[i]
    first = int(round(s / element))
    final.append(first)
    for i in range(1,len(arr)):
        final.append(int(round(first * arr[0] / arr[i])))
    return final
