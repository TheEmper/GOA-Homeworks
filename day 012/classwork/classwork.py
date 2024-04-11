# Basic List Slicing Syntax:
# a
# list_name[start:end:step]

# list_name: The name of the list you want to slice.
# start: The index of the first element you want to include in the slice.
# end: The index of the element just after the last element you want to include in the slice.
# step: The increment between indices. (Optional, defaults to 1)

#Examples:

# my_list = [1, 2, 3, 4, 5]

# Accessing a single element
# print(my_list[0])  # Output: 1

# # Accessing a range of elements
# print(my_list[1:4])  # Output: [2, 3, 4]

# my_list = [1, 2, 3, 4, 5]

# # Omitting start index (start from the beginning)
# print(my_list[:3])  # Output: [1, 2, 3]

# # Omitting end index (go till the end)
# print(my_list[2:])  # Output: [3, 4, 5]

# my_list = [1, 2, 3, 4, 5]

# # Negative indices count from the end of the list
# print(my_list[-3:])  # Output: [3, 4, 5]

# # Negative step reverses the list
# print(my_list[::-1])  # Output: [5, 4, 3, 2, 1]

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Using step to get every other element
# print(my_list[::2])  # Output: [1, 3, 5, 7, 9]

# # Reversing with a step
# print(my_list[::-1])  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

