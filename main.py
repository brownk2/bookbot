from stats import word_count, char_count, org_stats
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
 
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    count = word_count(get_book_text(path_to_book))
    # print(f"{count} words found in the document")
    chars = char_count(get_book_text(path_to_book))
    # print(chars)
    sort_list = org_stats(char_count(get_book_text(path_to_book)))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for i in sort_list:
        char = i["char"]
        num = i["num"]
        print(f"{char}: {num}")


main()