"""Given an array of strings, where each string may contain only lowercase English letters
 Write a function that groups the anagrams in the array together. The function should return a list of
 lists, where each inner list contains a group of anagrams"""


def group_anagrams(list1):
    word_vals = {}; # will use the word values as the keys and a list with all words of 
                    # the same value as the values
    anagrams = [];

    #Iterate for each word in the list and get it's numerical value
    for word in list1:
        word_val = 0;
        for letter in word:
            word_val += ord(letter)
        #add word into the list of that value
        if word_val in word_vals:
            word_vals[word_val].append(word);
        #otherwise create a new list with the word
        else:
            word_vals[word_val] = [word];

    
    for key in word_vals.keys():
        anagrams.append(word_vals[key]);

    return anagrams;



print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))