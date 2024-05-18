"""
SETS:
You have been given a list my_list with some duplicate values. 
Your task is to write a Python program that removes all the duplicates 
from the list using a set and then prints the updated list.

You need to implement a function remove_duplicates(my_list) 
that takes in the input list my_list as a parameter and returns a new list with no duplicates.

Your function should not modify the original list, 
instead, it should create a new list with unique values and return it."""

#simple method using a set to remove duplicates from a list
def remove_duplicates(list1):
    list_set = set(); #must use the set class to initialize an empty set, cannot use {}
    for num in list1:
        list_set.add(num); #a value can only be added once in a set
    n_list = []; # init empty list 
    n_list = list(list_set); #cast set to a list object
    return n_list;

my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
print(new_list)