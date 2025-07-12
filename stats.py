def count_words(file_contents):
    word_count = file_contents.split()
    print("----------- Word Count ----------")
    return len(word_count)

def count_characters(file_contents):
    character_counts = {}
    for char in file_contents:
        char = char.lower()
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    print("--------- Character Count -------")
    return character_counts

# Returns num value
def sort_on(dictionary):
    return dictionary["num"]

def sort_list(character_counts):
    sorted_list = []
    for char in character_counts:
        if char != ' ':
            new_dict = {"char": char, "num": character_counts[char]}
            sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return(sorted_list)
