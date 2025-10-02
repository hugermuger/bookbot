def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def count_words(book_text):
    return len(book_text.split())

def main():
    filepath = "books/frankenstein.txt"
    num_words = count_words(get_book_text(filepath))
    print(f"Found {num_words} total words")

main()