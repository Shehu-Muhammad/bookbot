def count_characters(text):
    characters = {}
    lowered_string = text.lower()
    result = []
    for c in lowered_string:
        if c.isalpha() == False:
            continue
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] += 1
    
    # Convert to a list of dictionaries
    char_list = [{'letter': k, 'count': v} for k, v in characters.items()]

    # Sort the list in descending order of count
    sorted_char_list = sorted(char_list, key=sort_on, reverse=True)

    for item in sorted_char_list:
        result.append(f"The '{item['letter']}' character was found {item['count']} times")
    return '\n'.join(result)

def count_words(text):
    words = text.split()
    count = len(words)
    return f"{count} words found in the document\n"
