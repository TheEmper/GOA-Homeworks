# 8 kyu

# 1
def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)


# 2 rock, paper, scissors

def rps(p1, p2):
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p2 == "scissors" and p1 == "paper":
        return "Player 2 won!"
    elif p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    elif p2 == "scissors" and p1 == "rock":
        return "Player 1 won!"
    elif p1 == p2:
        return "Draw!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p2 == "paper" and p1 == "rock":
        return "Player 2 won!"
    
# 3

def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return 2 * (l+w)
    
# 7 kyu

# 1

def remove_url_anchor(url):
    return url.split('#')[0]

# 2

# write the function is_anagram
def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    
    test = sorted(test)
    original = sorted(original)
    
    return test == original

# 3

def mygcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
    
# 6 kyu

# 1

def expanded_form(num):
    num_str = str(num)
    expanded = []
    for i in range(len(num_str)):
        digit = num_str[i]
        if digit != '0':
            expanded.append(digit + '0' * (len(num_str) - i - 1))
    return ' + '.join(expanded)


# 2

# ????????????????????\


# 3



# 5 kyu

def pig_it(text):
    words = text.split()
    pigged_words = []
    for word in words:
        if word.isalpha():
            pigged_word = word[1:] + word[0] + 'ay'
            pigged_words.append(pigged_word)
        else:
            pigged_words.append(word)
    return ' '.join(pigged_words)