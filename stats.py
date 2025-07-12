def count_words(file_contents):
    word_count = file_contents.split()
    return len(word_count)

def count_characters(file_contents):
    character_counts = {}
    for char in file_contents:
        char = char.lower()
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts
