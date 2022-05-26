# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Added here 
    with open(filename) as f:
        contents = f.read()
        return contents
        print(contents)
    


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Added here
    # clean text by removing white spaces; convert to lower key for uniformity and split sentences into words
    clean_text = text.lower().strip().split()

    # remove punctuations
    import string
    table = str.maketrans('', '', string.punctuation)
    stripped = [word.translate(table) for word in clean_text]
    
     # dictionary comprehension to provide key, value chain for word and word count
    dict = {word : stripped.count(word) for word in stripped}
    return dict
    print (dict)