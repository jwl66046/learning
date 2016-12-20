#!/usr/bin/env python3

"""

John's Note:

As of this version, the function appears to be working.

Look for a way to simplify and remove all the debugs

"""

import random

my_list = random.sample(range(1, 100), 15)
my_list2 = random.sample(range(1, 100), 16)

def median(lst):
    result = 0
    sort_list = sorted(lst)
    print("This is the sort_list variable:\t\t" + str(sort_list))
    
    e_or_o = len(sort_list)/ 2
    print("Result of e_or_o variable:\t\t" + str(e_or_o))

    if e_or_o % 2 == 1:
        print("The result is even")
        first = sort_list[int(e_or_o)]
        print("\tFirst equals - " + str(first))
        second = sort_list[int(e_or_o) - 1]
        print("\tSecond equals - " + str(second))
        result = (first + second) / 2.0
    else:
        print("The result is odd")
        result = sort_list[int(e_or_o)]
    return result



### Debugging below    
print('''\n
Running List 1, odd number:
\n''')
      
print("RESULT: " + str(median(my_list)))


print('''\n
Running List 2, even number:
\n''')

print("RESULT:" + str(median(my_list2)))


