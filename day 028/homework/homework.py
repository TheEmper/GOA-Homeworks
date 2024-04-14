# 1 7kyu

def solution(text, ending):
    return text[-len(ending):] == ending

# 2 7kyu

def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

# 3 7kyu

# ?

# 4 7kyu

def reverse_words(text):
    words = text.split(" ")
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

# 5 7kyu

def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b




# 1 6kyu

# ?

# 2 6kyu

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# 3 6kyu

def pyramid(n):
    return [[1] * (i+1) for i in range(n)]


