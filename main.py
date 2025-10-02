from stats import get_num_words, get_num_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    filepath = "books/frankenstein.txt"
    num_words = get_num_words(get_book_text(filepath))
    print(f"Found {num_words} total words")
    print(get_num_characters(get_book_text(filepath)))

main()