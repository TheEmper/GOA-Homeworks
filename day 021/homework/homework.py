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

# 5: Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))


# 6 You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item

def likes(names):
    likes = len(names)
    other_likes = len(names) - 2
    if likes == 0:
        return "no one likes this"
    elif likes == 1:
        return f"{names[0]} likes this"
    elif likes == 2:
        return f"{names[0]} and {names[1]} like this"
    elif likes == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif likes >= 4:
        return f"{names[0]}, {names[1]} and {other_likes} others like this"
    
# 7 

def solution(number):
    natural_numbers = []
    multiples = []
    
    if number == 0:
        return 0
    
    for i in range(number):
        natural_numbers.append(i)
    for n in natural_numbers:
        if n % 3 == 0 or n % 5 == 0:
            multiples.append(n)
        elif n % 3 == 0 and n % 5 == 0:
            return 0
        
    return sum(multiples)