import sys
from stats import get_number_of_words, get_character_counts, to_sorted_dictionary_entry_list

"""
python3 main.py
python3 main.py books/frankenstein.txt
python3 main.py books/mobydick.txt
python3 main.py books/prideandprejudice.txt
"""

def print_book_report(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    print("----------- Word Count ----------")
    num_words = get_number_of_words(filepath)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    character_counts = get_character_counts(filepath)
    sorted_dictionary_entry_list = to_sorted_dictionary_entry_list(character_counts)

    for entry in sorted_dictionary_entry_list:
        print(f"{entry['letter']}: {entry['count']}")

    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    print_book_report(filepath)

main()
