"""You are given two lists of integers, arr1 and arr2, 
and a target integer value, target. 
Your task is to find all pairs of numbers 
(one from arr1 and one from arr2) whose sum equals target."""

#simple method that uses a set to find pairs of values from each list that add up to the
#target value
def find_pairs(list1, list2, target):
    set1 = set(list1); # convert one of the list to a set
    pairs = []; #init empty list
    for num in list2: #iterate through the second list
        if (target - num) in set1: #check whether the compliment to the number is in the set
            pairs.append((target - num, num)); 
    return pairs;

 
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)
