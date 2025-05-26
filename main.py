def main():
    book = get_book_text("./books/frankenstein.txt")
    get_words(book)

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    
def get_words(word):
    count = word.split()
    len_count = len(count)
    print(f"{len_count} words found in the document.")
          
main()