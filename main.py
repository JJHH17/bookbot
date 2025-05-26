from stats import get_words, get_chars

def main():
    book = get_book_text("./books/frankenstein.txt")
    chars = get_chars(book)
    get_words(book)
    print(chars)

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    
main()