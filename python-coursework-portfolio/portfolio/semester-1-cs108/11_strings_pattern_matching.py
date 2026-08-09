'''
Topic: Strings & pattern matching -- Pig Latin translation and a word search
solver (horizontal + vertical), built without built-in search/replace methods.
'''

#######################################
# Count vowels in a word
#######################################
def count_vowels(word):
    vowels = 'aeiouAEIOU'
    total = 0
    for ch in word:
        if ch in vowels:
            total += 1
    return total

#######################################
# Capitalize the 2nd and last letter of a word
#######################################
def cap2(text):
    if len(text) == 0:
        return ""
    if len(text) == 1:
        return text.lower()
    chars = list(text.lower())
    chars[1] = chars[1].upper()
    chars[-1] = chars[-1].upper()
    return ''.join(chars)

#######################################
# Translate a single word to Pig Latin
#######################################
def pig_latin(word):
    vowels = 'aeiouAEIOU'
    if word[0] in vowels:
        result = word + 'ay'
    else:
        result = ''
        idx = 1
        while idx < len(word):
            result += word[idx]
            idx += 1
        result += word[0] + 'ay'
    return result

#######################################
# Translate a full sentence to Pig Latin
#######################################
def pig_latin_sentence(sentence):
    words = sentence.split()
    result = ''
    for w in words:
        pig_word = pig_latin(w)
        if result == '':
            result = pig_word
        else:
            result += ' ' + pig_word
    return result

#######################################
# Count occurrences of a set of substrings within a word (case-insensitive)
#######################################
def count_these(word, char_list):
    total = 0
    word_lower = ''
    for ch in word:
        word_lower += ch.lower()

    for target in char_list:
        target_lower = ''
        for ch in target:
            target_lower += ch.lower()
        idx = 0
        while idx <= len(word_lower) - len(target_lower):
            match = True
            for j in range(len(target_lower)):
                if word_lower[idx + j] != target_lower[j]:
                    match = False
            if match:
                total += 1
            idx += 1
    return total

#######################################
# Search for a word horizontally in a letter grid
#######################################
def hidden_word_horiz(box_of_letters, word):
    for row in box_of_letters:
        idx = 0
        while idx <= len(row) - len(word):
            match = True
            for j in range(len(word)):
                if row[idx + j] != word[j]:
                    match = False
            if match:
                return True
            idx += 1
    return False

#######################################
# Search for a word vertically in a letter grid
#######################################
def hidden_word_vert(box_of_letters, word):
    for col in range(5):
        idx = 0
        while idx <= 5 - len(word):
            match = True
            for j in range(len(word)):
                if box_of_letters[idx + j][col] != word[j]:
                    match = False
            if match:
                return True
            idx += 1
    return False

#######################################
# Search a letter grid for a hidden word (horizontal or vertical)
#######################################
def hidden_word(box_of_letters, word):
    if hidden_word_horiz(box_of_letters, word):
        return True
    elif hidden_word_vert(box_of_letters, word):
        return True
    else:
        return False
