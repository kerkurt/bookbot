from stats import get_count_words, get_count_each_character

def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    get_count_words(book_text)
    char_count = get_count_each_character(book_text)
    for char, count in char_count.items():
        print(f"'{char}': {count}")
    
def get_book_text(filePath):
    with open(filePath) as file:
        return file.read()
    
main()