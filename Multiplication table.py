'''
[+]Your task, is to create NxN multiplication table, of size provided in parameter.

[+]for example, when given size is 3:
  1 2 3
  2 4 6
  3 6 9
'''

#solution:
def multiplication_table(size):
    table = []
    for i in range(size):
        table.append([])
        for k in range(size):
            table[i].append((i+1)*(k+1))
    return table
