def get_num_words():
    words = content.split()
    word_count = len(words)
    print(word_count,"words found in the document")

def count_characters(text):
    text = text.lower()
    char_counts = {}
    
    for char in text:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    return char_counts

def sorted_dictionary(char_counts, descending=True):
    return sorted(char_counts.items(), key=lambda item: item[1], reverse=descending)


