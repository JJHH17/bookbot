from stats import get_words, get_chars, sorted_dict

def main():
    print("============ BOOKBOT ============")
    book = get_book_text("./books/frankenstein.txt")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    words = get_words(book)
    print("--------- Character Count -------")
    chars = get_chars(book)
    char_nums = sorted_dict(chars)
    for char in char_nums:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    
main()