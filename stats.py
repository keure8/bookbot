def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    lower_text = text.lower()
    char_dict = {}
    for char in lower_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def expand_dict(dictionary):
    expanded_dict = []
    for key, value in dictionary.items():
        expanded_dict.append({"char": key, "num": value})
    return expanded_dict

def sort_on(items):
    return items["num"]

