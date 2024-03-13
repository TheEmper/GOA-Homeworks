# # pirveli davaleba
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]

print(nums[0] * nums[6])
print(nums[4] + nums[5])
print(nums[3] / nums[1])
print(nums[7] - nums[4])

# meore davaleba

shopping_list = ["", "", ""]

shopping_list[0] = "Banana"
shopping_list[1] = "Ketchup"
shopping_list[2] = "Bread"

print(shopping_list)

shopping_list[0] = "Apple"
shopping_list[1] = "Mayo"
shopping_list[2] = "Eggs"

print(shopping_list)

# mesame davaleba

fast_food = ["Mcdonalds", "KFC", "Wendy's", "Domino's pizza"]

fav_place = int(input("What's your favorite fast food restaurant?(Enter a number from 0 to 3): "))

if fav_place > 3 or fav_place < 0:
  print("Error")
else:
  print("Your favorite place is: ", fast_food[fav_place])

