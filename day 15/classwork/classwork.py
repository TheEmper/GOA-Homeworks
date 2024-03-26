def greetings(name):
  print("Hello",name)

greetings("Sandro")

# davaleba 1

def addition(num1, num2):
  print(num1 + num2)

addition(1, 2)

def multiplication(num1, num2):
  print(num1 * num2)

multiplication(1, 2)


def subtraction(num1, num2):
  print(num1 - num2)

subtraction(1, 2)

def division(num1, num2):
  print(num1 / num2)

division(1, 2)

#davaleba 2

def area(width, height):
  print("The area of the rectangle:",width * height)

area(5, 3)

# davaleba 3

def perimeter(side1, side2, side3, side4):
  print("The perimeter of the rectangle is:",side1 + side2 + side3 + side4)

perimeter(5, 3, 6, 7)

# davaleba 4

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    print("The sum of the numbers is:",total)

my_list = [1, 2, 3, 4, 5]
calculate_sum(my_list)

# davaleba 5

def min_max(numbers):

    min_num = numbers[0]
    max_num = numbers[0]

    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    print("Minimum number:", min_num)
    print("Maximum number:", max_num)

number_list = [4, 7, 1, 8, 6]
min_max(number_list)

# a



