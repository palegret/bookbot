SORT_KEY = "count"


def get_word_count(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}

    for c in text:
        lowered = c.lower()
        
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
            
    return chars


def sort_on(dict):
    return dict[SORT_KEY]


def chars_dict_to_sorted_list(char_count_dict):
    sorted_list = []

    for char in char_count_dict:
        sorted_list.append({
            "char": char, 
            "count": char_count_dict[char]
        })

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
