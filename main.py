import sys

from stats import (
    chars_dict_to_sorted_list,
    get_chars_dict,
    get_word_count,
)

def main():
    book_path = get_book_path()
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    chars_dict = get_chars_dict(book_text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)


def get_book_path():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    return book_path


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, word_count, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue

        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")



"""
python3 main.py
python3 main.py books/frankenstein.txt
python3 main.py books/mobydick.txt
python3 main.py books/prideandprejudice.txt
"""

main()
