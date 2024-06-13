# 1
def sum_two_smallest_numbers(numbers):
   numbers.sort()
   return numbers[0] + numbers[1]

# 2

def max_multiple(divisor, bound):
    nums = []
    for i in range(bound + 1):
        if i % divisor == 0:
            nums.append(i)
            
    return nums[-1]

# 3

def get_even_numbers(arr):
    liist = []
    for num in arr:
        if num % 2 == 0:
            liist.append(num)
    return liist

# 4

def check_exam(arr1,arr2):
    score = 0
    for correct, student in zip(arr1, arr2):
        if student == "":
            continue
        if student == correct:
            score += 4
        else:
            score -= 1
    return max(score, 0)

# 5

def row_weights(array):
    team1_weight = sum(array[::2]) 
    team2_weight = sum(array[1::2])  
    return (team1_weight, team2_weight)