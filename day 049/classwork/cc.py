# 1

def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count  

# 2
def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))

# 3

def filter_list(l):
    answer = []
    for i in l:
        if type(i) == int:
            answer.append(i)
    return answer

# 4

def find_it(seq):
    for num in seq:
        i = seq.count(num)
        if i % 2 != 0:
            return num
        
# 5

def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n