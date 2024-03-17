# # davaleba 1
user_info = []

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
residence = input("Enter your place of residence: ")

user_info.append(first_name)
user_info.append(last_name)
user_info.append(age)
user_info.append(residence)

print("1:", user_info[0:2])
print("2:", user_info[1:3])
print("3:", user_info[0:3])
print("4:", user_info[1:])

# davaleba 2

nums = []

negative_num = int(input("Enter a negative number: "))

for i in range(negative_num, 0):
  nums.append(i)

print(nums)

# # davaleba 3

full_name = "Sandro Miqeladze"
first_name = full_name[:6]
last_name = full_name[-9:]

print(first_name)
print(last_name)

# davaleba 4

movies = ["Whispers of the Forgotten", "Neon Dreamscape", "Eternal Echoes", "Midnight Mirage", "Rogue Constellation"]

print(movies[1:3])
print(movies[:3])
print(movies[2:])

#neg sliciing

print(movies[-4:-2])
print(movies[-5:-2])
print(movies[-3:])

# davaleba 5

academy = input("What academy do you go to?: ")

if academy[0] == "G":
  print("GOA is the correct choice.")
else:
  print("Wrong choice.")



