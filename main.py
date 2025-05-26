from stats import get_words

def main():
    book = get_book_text("./books/frankenstein.txt")
    get_words(book)

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    
main()