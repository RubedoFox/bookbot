import sys

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

from stats import get_num_words
from stats import count_characters
from stats import sorted_dictionary

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filename = sys.argv[1]
    
    content = get_book_text(filename)
    #print(content)
    words = content.split()
    word_count = len(words)    
    character_counts = count_characters(content)
    sorted_counts = sorted_dictionary(character_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found",word_count,"total words")
    print("--------- Character Count -------")
    for char, count in sorted_counts:
        print(f"{char}: {count}")
    print("============= END ===============")

main()