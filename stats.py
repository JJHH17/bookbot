def get_words(word):
    count = word.split()
    len_count = len(count)
    print(f"Found {len_count} total words")

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
    sort = sorted(sorted_list, key=lambda x: x["num"], reverse=True)

    return sort