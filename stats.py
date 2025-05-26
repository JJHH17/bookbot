def get_words(word):
    count = word.split()
    len_count = len(count)
    print(f"{len_count} words found in the document.")

def get_chars(word):
    frequency = {}
    # Convert to lowercase
    words = word.lower()
    # Get individual words
    words = list(words)
    # Loop to populate dictionary
    for char in words:
        if char in frequency:
            frequency[char] += 1 
        else:
            frequency[char] = 1
    return frequency