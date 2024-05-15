"""Problem: Given an array of integers nums and a target integer target, 
find the indices of two numbers in the array that add up to the target.

The main challenge here is to implement this function in one pass through the array. 
This means you should not iterate over the array more than once. 
Therefore, your solution should have a time complexity of O(n), 
where n is the number of elements in nums. """

"""This function iterates through the parameter list
    each value is subtracted from the target
    the resulting value is search in the hash table
    if the value is present in the hash table, then a
    a pair of values that sum up to the target value has been found and should be returned
    otherwise add the value as the key and the index as the value
"""
def two_sum(list1, target):
    values = {}; #empty hash table

    
    for i in range(len(list1)):
        partner = target - list1[i]; #get difference
        if partner in values: # check if the value is present in the hash table
            return [values[partner], i]; # return the index of both values
        else:
            values[list1[i]] = i;   # add value to the hash_table
    return [] #return empty list if no target pairs is found. 

print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )