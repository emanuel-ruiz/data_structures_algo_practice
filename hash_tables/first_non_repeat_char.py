#Returns the first letter in the passed in string that does not repeat
def first_non_repeating_char(word):
    repeats = {};
    for letter in word:
        if letter in repeats:
            repeats[letter] = True;
        else: 
            repeats[letter] = False; 

    for letter in word:
        if repeats[letter] == False:
            return letter;

    return None;

print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""