from stats import count_words, count_characters, sorted_list
import sys

book = None
# Book Sys selection
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book> ")
    sys.exit(1)
else:
    book = sys.argv[1]


def read_book(path):
    with open(path) as f:
        content = f.read()
    return content


def main():
    content = read_book(book)
    counted_words = count_words(content)
    characters = count_characters(content)
    sorted = sorted_list(characters)

    # Print Report

    print(f"============ BOOKBOT ============\nAnalyzing book found at {book}...")
    print(f"----------- Word Count ----------\nFound {counted_words} total words")
    print("--------- Character Count -------")
    for i in sorted:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")


main()
