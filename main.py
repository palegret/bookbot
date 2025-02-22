from stats import get_number_of_words, get_character_counts

BOOKS_ROOT = "books"

def main():
    filepath = f"{BOOKS_ROOT}/frankenstein.txt"
    num_words = get_number_of_words(filepath)
    print(f"{num_words} words found in the document")
    character_counts = get_character_counts(filepath)
    print(character_counts)
main()
