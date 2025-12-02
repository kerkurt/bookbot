def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(book_text)

def get_book_text(filePath):
    with open(filePath) as file:
        return file.read()
    
main()