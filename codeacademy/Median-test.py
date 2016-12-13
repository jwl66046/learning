import random

my_list = random.sample(range(1, 100), 15)
my_list2 = random.sample(range(1, 100), 16)

def median(lst):
    sort_list = sorted(lst)
    print("This is the sort_list variable: \n\t" + str(sort_list))
    
    e_or_o = len(sort_list)/ 2
    print("Result of sort_list: \t" + str(e_or_o))

    if e_or_o % 2 == 0:
        print("The result is even")
        first = len(sort_list) / 2.0
        print("\tFirst equals - " + str(first))
        second = len(sort_list) - 1 / 2.0
        print("\tSecond equals - " + str(second))

    else:
        print("The result is odd")
        



print('''\n\n\n
Running List 1, odd number:
\n''')
      
median(my_list)



print('''\n\n\n
Running List 2, even number:
\n''')

median(my_list2)

