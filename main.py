from stats import count_words, count_characters
path_to_frankenstein = "books/frankenstein.txt"

def sort_on(dict):
    return dict['count']

def main():
    print(f"--- Begin report of {path_to_frankenstein} ---")
    with open(path_to_frankenstein) as f:
        file_contents = f.read()
        #print(file_contents)
        print(count_words(file_contents))
        print(count_characters(file_contents))
    print("--- End report ---")
main()

