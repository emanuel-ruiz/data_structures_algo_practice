"""Given an unsorted array of integers, 
write a function that finds the length of the  longest_consecutive_sequence 
(i.e., sequence of integers in which each element is one greater than the previous element). """

def longest_consecutive_sequence(list1):
    set_list = set(list1);
    longest = 0;
    for num in list1:
        length = 0;
        temp = num;
        while temp in set_list:
            length += 1
            temp = temp + 1;
        if length > longest:
            longest = length;
    return longest;

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )