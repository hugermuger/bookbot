from stats import get_num_words, get_num_characters, sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        num_words = get_num_words(get_book_text(filepath))
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        num_dic = get_num_characters(get_book_text(filepath))
        sorted_num_dic = sorted_list(num_dic)
        for i in sorted_num_dic:
            if i["name"].isalpha() and i["name"] != None:
                print(f"{i["name"]}: {i["num"]}")
        print("============= END ===============")

main()