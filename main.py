import sys
from stats import count_words, count_characters
# Check if a book path was provided
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Get the book path from command-line arguments
path_to_book = sys.argv[1]

def main():
    print(f"--- Begin report of {path_to_book} ---")
    with open(path_to_book) as f:
        file_contents = f.read()
        print(count_words(file_contents))
        print(count_characters(file_contents))
    print("--- End report ---")
main()

