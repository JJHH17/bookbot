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
    # Loop to pgoldbridgeopulate dictionary
    for char in words:
        if char in frequency:
            frequency[char] += 1 
        else:
            frequency[char] = 1
    return frequency

def sorted_dict(input):
    sorted_list = [{"char": k, "num": v} for k, v in input.items()]
    print(sorted_list)

sorted_dict({"hello": 1, "goodbye": 10, "howdy": 10})