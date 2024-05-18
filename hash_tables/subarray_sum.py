"""
Given an array of integers nums and a target integer target, 
write a Python function called subarray_sum 
that finds the indices of a contiguous subarray in nums that add up to the target sum 
using a hash table (dictionary).

Your function should take two arguments:

    nums: a list of integers representing the input array

    target: an integer representing the target sum


Your function should return a list of two integers representing 
the starting and ending indices of the subarray that adds up to the target sum. 
If there is no such subarray, your function should return an empty list."""

def subarray_sum(list1, target):
    subarray = []; #initialize empty list
    sums = {0:-1}; #initialize hash table with 0 and -1 for the instance that the first element is the target element
                   #Logic: the start of the target subarray starts after the index in the hash table
    total_sum = 0; 
    for i, num in enumerate(list1):
        total_sum += num; 
        if(total_sum - target) in sums:
            subarray.append(sums[total_sum - target] + 1); # value has been found in the hash table 
                                                           # append the index after the hash value
            subarray.append(i);
            return subarray;
        else:
            sums[total_sum] = i; #each index will have it's corresponding total sum
    return subarray;

nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )
nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )

    