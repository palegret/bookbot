SORT_KEY = "count"
SPACE = " "

def get_book_text(filepath):
    file_contents = None

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def get_number_of_words(filepath):
    book_text = get_book_text(filepath)
    words = book_text.split(sep=SPACE)
    num_words = len(words)
    return num_words

def get_character_counts(filepath):
    book_text_lower = get_book_text(filepath).lower()
    character_counts = {}

    for character in book_text_lower:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1

    return character_counts

def sort_on(dictionary):
    return dictionary[SORT_KEY]

"""
# List comprehension example.
def to_dictionary_entry_list(dictionary):
    return [{"letter": key, SORT_KEY: value} for key, value in dictionary.items()]
"""

def to_sorted_dictionary_entry_list(dictionary):
    dictionary_entry_list = []

    for entry in dictionary.items():
        key, value = entry

        if not key.isalpha():
            continue

        dictionary_entry_list.append({
            "letter": key,
            SORT_KEY: value
        })

    dictionary_entry_list.sort(reverse=True, key=sort_on)

    return dictionary_entry_list
