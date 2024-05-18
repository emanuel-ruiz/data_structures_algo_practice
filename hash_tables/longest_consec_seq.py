"""Given an unsorted array of integers, 
write a function that finds the length of the  longest_consecutive_sequence 
(i.e., sequence of integers in which each element is one greater than the previous element). """

#method converts list into a set 
#this allows the ability to check in O(1) time if the following value is present in the list
def longest_consecutive_sequence(list1):
    set_list = set(list1);
    longest = 0; # longest value
    for num in list1:
        length = 0; #length of current sequence
        while num in set_list: #loop until the sequence is broken
            length += 1
            num = num + 1;
        if length > longest: #set longest if current lenght sequence is greater. 
            longest = length;
    return longest;

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )