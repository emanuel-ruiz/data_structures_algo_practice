"""Given an array of strings, where each string may contain only lowercase English letters
 Write a function that groups the anagrams in the array together. The function should return a list of
 lists, where each inner list contains a group of anagrams"""

def group_anagrams(wordList):
    finalList = [];
    for i in range(len(wordList)):
        word = {}
        for letter in wordList[i]:
            
    

def print_dictionaries(dictlist):
    for key in dictlist.keys():
        print(key + ":");
        for lKey in dictlist[key].keys():
            print(lKey);


group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])