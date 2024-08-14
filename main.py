def main():
    # replace "book/frankenstein.txt" with the source of your book
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = get_word_count(text)
    sorted_dict = char_sort(get_char_count(text))

    print(f"--- Begin report of {book_path} ---")
    print(f"The document contains {total_words} words!\n")
    for sort in sorted_dict:
        print(f"The {sort['letter']} character was found {sort['count']} times")
    print("\n--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    chars = {}
    lowered = text.lower()
    for lower in lowered:
        if lower in chars:
            chars[lower] += 1
        else:
            chars[lower] = 1
    return chars

def sort_on(d):
        return d["count"]

def char_sort(chars):
    char_list = []
    for char in chars:
        if char.isalpha() == True:
            count = chars[char]
            new_dict = {"letter": char, "count":count}
            char_list.append(new_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list



main()
