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
