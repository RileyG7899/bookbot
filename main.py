import sys
from stats import count_words
from stats import count_characters
from stats import sort_list
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    print("============ BOOKBOT ============")
    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    print(f"Analyzing book found at {filepath}")
    word_count = count_words(file_contents)
    print(f"Found {word_count} total words")
    character_counts = count_characters(file_contents)
    #print(file_contents)
    #print(character_counts)
    sorted_list = sort_list(character_counts)
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

main()