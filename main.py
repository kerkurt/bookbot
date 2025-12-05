from stats import get_count_words, get_count_each_character, sort_dictionary_by_value

def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {book_path}...")
    print("----------- Word Count ----------")
    get_count_words(book_text)
    print("------- Character Count --------")
    char_count = get_count_each_character(book_text)
    char_count = sort_dictionary_by_value(char_count)
    for char, count in char_count.items():
        if char.isalpha():
            print(f"{char}: {count}")
    
def get_book_text(filePath):
    with open(filePath) as file:
        return file.read()
    
main()