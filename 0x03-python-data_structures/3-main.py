#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
   for i in range(len(my_list) - 1, -1, -1):
    print(str.format("%d" % my_list[i]))
      
>>> print_reversed_list_integer([1, 2, 3, 4, 5])
