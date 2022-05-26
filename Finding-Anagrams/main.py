# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(a, b):
    # strip the strings of leading and trailing white spaces
    # convert strings to lower case for uniformity
    # remove any spaces within string
    a_clean = a.strip().lower().replace(" ", "")
    b_clean = b.strip().lower().replace(" ", "")
    
    # sort the string
    a_sort = sorted(a_clean)
    b_sort = sorted(b_clean)
    
    # assign the length of each word to a variable name - having excluded spaces
    a_len = len(a_sort)
    b_len = len(b_sort)
    
    # insert condition - if lengths of strings are equal, check if the sorted strings are equal
    if a_len == b_len:
        if a_sort == b_sort:
            return True
            print (True)
        else:
            return False
            print (False)
    else:
        return False
        print (False)