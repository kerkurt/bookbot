def get_count_words(text):
    words = text.split()
    print(f"Found {len(words)} total words")

def get_count_each_character(text):
    char_count = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1
    return char_count

def sort_dictionary_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))