from stats import count_words, count_characters, report_dict_formating
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    rltv_file_path = sys.argv[1]
    text = get_book_text(rltv_file_path)
    num_words = count_words(text)
    characters = count_characters(text)
    report_characters = report_dict_formating(characters)
    print_report(num_words, report_characters, rltv_file_path)

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read() 
    return file_contents

def print_report(num_words, report_characters, file_path):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {file_path}...")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print("--------- Character Count -------")
    for item in report_characters:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")



main()