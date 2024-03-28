def initials(name):
  first_name, last_name = name.split()
  first_initial, second_initial = first_name[0], last_name[0]
  print(f"{first_initial}.{second_initial}")

initials("Sandro Miqeladze")



# 2

def avg(numbers_list):
  average_num = sum(numbers_list) / len(numbers_list)
  print(average_num)


numbers_list = [1, 2, 4, 7, 8]

avg(numbers_list)


# 3 

def palindrom(word):
  if word == word[::-1]:
    print("Is a palindrom")
  else:
    print("Is not a palindrom")

palindrom("level")
palindrom("ugabuga")


# 4

def remove_space(word):
  word_1 = word.replace(" ", "")
  print(word_1)

remove_space("Goal Oriented")

# 5

def big_function(numbers):
  count_neg = 0
  sum_numbers = 0

  for num in numbers:
    if num < 0:
      count_neg += 1
    else:
      sum_numbers += num

  print(f"Sum of the positive numbers is {sum_numbers} and the amount of negative numbers in the list is {count_neg}")

numbers = [4, -3, -5, -22, 6, 8 ,9, 11]
big_function(numbers)
