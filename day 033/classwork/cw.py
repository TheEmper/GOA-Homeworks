
# 7 KYU

# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.


def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        for digit in pin:
            if not '0' <= digit <= '9':
                return False
        return True
    else:
        return False
    
# The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

#To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.


def open_or_senior(data):
    result = []
    for i in data:
        age, handicap = i
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result    

# Write a function that returns both the minimum and maximum number of the given list/array.

def min_max(lst):
    return [min(lst), max(lst)]

# Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.

# a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.

# The four operators are "add", "subtract", "divide", "multiply".

def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b
    

# Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.

def capitals(word):
    result = []
    for i in range(len(word)):
        if word[i].isupper():
            result.append(i)
            
    return result



# 6 KYU


# 1

def array_diff(a, b):
    result = []
    for num in a:
        if num not in b:
            result.append(num)
    return result

# 2

# 3 Write a method (or function, depending on the language) that converts a string to camelCase, that is, all words must have their first letter capitalized and spaces must be removed.

def camel_case(s):
    listi = s.split(" ")
    result = []
    for i in listi:
        j = i.capitalize()
        result.append(j)
    return "".join(result)


# final boss / 5 kyu

def variance(numbers): 
    mean = sum(numbers) / len(numbers)
    
    squared = [(i - mean) ** 2 for i in numbers]
    
    
    sum_squar = sum(squared)
    
    return sum_squar / len(numbers)


