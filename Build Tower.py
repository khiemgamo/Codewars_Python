'''
Build Tower
[+]Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

[+]Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Ruby: returns an Array;
Lua: returns a Table;
Have fun!

[+]for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]
'''

#solution:
def tower_builder(n_floors):
    tower = []
    for i in range(1,n_floors+1):
        floor = ""
        floor += (" " * (n_floors-i)) + ("*" * (i * 2 - 1)) + (" " * (n_floors-i))
        tower.append(floor)
    return tower

#solution 2:
def tower_builder(n_floors):
    tower = []
    for i in range(1,n_floors+1):
        tower.append(("*" * (i * 2 -1)).center(n_floors * 2 -1))
    return tower
