from stats import get_count_words

def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    get_count_words(book_text)

def get_book_text(filePath):
    with open(filePath) as file:
        return file.read()
    
main()