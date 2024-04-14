# 1
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

# 2

def friend(x):
    friends = []
    for i in x:
        if len(i) == 4:
            friends.append(i)
    return friends

# 3

def find_short(s):
    words = s.split()
    return min(len(word) for word in words)

# 4

def get_middle(s):
    if len(s) % 2 == 0:
        middle_left_index = len(s) // 2 - 1
        middle_right_index = len(s) // 2
        return s[middle_left_index:middle_right_index + 1]
    else:
        middle_index = len(s) // 2
        return s[middle_index]

# 5

def high_and_low(numbers):
    numbers_list = [int(num) for num in numbers.split(" ")]
    min_num = min(numbers_list)
    max_num = max(numbers_list)
    high_low = str(max_num) + " " + str(min_num)
    return high_low


