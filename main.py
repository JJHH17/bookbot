from stats import get_words, get_chars, sorted_dict

def main():
    book = get_book_text("./books/frankenstein.txt")
    chars = get_chars(book)
    char_nums = sorted_dict(chars)
    print(chars)

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    
main()