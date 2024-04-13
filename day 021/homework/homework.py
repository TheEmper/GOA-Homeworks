# 1: Given a non-empty array of integers, return the result of multiplying the values together in order.
def grow(arr):
    total = 1
    for i in arr:
        total *= i
    return total

# 2: Write function bmi that calculates body mass index (bmi = weight / height2).
def bmi(weight, height):
    bmi = weight / (height * height)
    if bmi <= 18.5: 
        return "Underweight"
    
    if bmi <= 25.0: 
        return "Normal"

    if bmi <= 30.0: 
        return "Overweight"

    if bmi > 30: 
        return "Obese"
    
# 3: Return the number (count) of vowels in the given string.

#We will consider a, e, i, o, u as vowels for this Kata (but not y).

#The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    vowels = 'aeiou'
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count

# 4:

def square_digits(num):
    num_str = str(num)
    result = ""
    for digit in num_str:
        result += str(int(digit) ** 2)
    return int(result)

# 5:

