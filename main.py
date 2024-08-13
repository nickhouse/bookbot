def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = get_word_count(text)
    print(f"The document contains {total_words} words!")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

main()
