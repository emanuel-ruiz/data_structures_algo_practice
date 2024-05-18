"""Write a function called has_unique_chars that takes a string as 
input and returns True if all the characters in the string are unique, 
and False otherwise. """

#simple method using a set to check whether all characters are unique
def has_unique_chars(word):
    word_set = set();
    for letter in word:
        if letter in word_set: 
            return False;
        else:
            word_set.add(letter);
    return True;

print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False
