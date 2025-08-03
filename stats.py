def sort_on(items):
    return items["num"]

def count_words(text):
    num_words = len(text.split())
    return num_words

def count_characters(text):
    num_characters = {}
    for character in text:
        character = character.lower()
        if character in num_characters:
            num_characters[character] += 1
            continue
        num_characters[character] = 1
    return num_characters

def report_dict_formating(characters):
    report_list = []
    for character in characters:
        char_data = {"char": character, "num": characters[character]}
        report_list.append(char_data)
    report_list.sort(reverse=True, key=sort_on)
    return report_list