# 6 kyu

# 1 The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

def duplicate_encode(word):
    lower_case = word.lower()
    dupped = ""
    for char in lower_case:
        count = lower_case.count(char)
        if count > 1:
            dupped += ")"
        else:
            dupped += "("
    return dupped

# 2 A  pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant). Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

def is_pangram(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    low = st.lower()
    
    for char in alphabet:
        if low.find(char) == -1:
            return False
        
    return True

# 5 kyu Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

# If a string contains all repeating characters, it should return an empty string ("");

#  Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character.

def first_non_repeating_letter(s):
    for char in s:
        if s.lower().count(char.lower()) == 1:
            return char
    return ""



