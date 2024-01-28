''' Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line. '''

def letters_in_either_word(word1, word2):
    return sorted(list(set(word1) | set(word2)))

def letters_in_both_words(word1, word2):
    return sorted(list(set(word1) & set(word2)))

def letters_in_one_word_only(word1, word2):
    return sorted(list(set(word1) ^ set(word2)))

word1 = "Task"
word2 = "Program"

print(f"Letters that appear in at least one of the two words: {letters_in_either_word(word1, word2)}")
print(f"Letters that appear in both words: {letters_in_both_words(word1, word2)}")
print(f"Letters that appear in either word, but not in both: {letters_in_one_word_only(word1, word2)}")