# 1 

name = input("Enter a name: ")
lowercase_name = name.lower()
if name == lowercase_name:
    print("The name is already lowercase.")
else:
    print("The name is not lowercase.")

# 2

def has_lowercase(word):
    for letter in word:
        if letter.islower():
            return True
    return False

word = input("Enter a word: ")
counter = 1
while has_lowercase(word):
    print("The word contains lowercase letters. Please enter another word.")
    word = input("Enter a word: ")
    counter += 1

print("No lowercase letters found in the word.")
print("Number of times the user had to enter the word:", counter)

# 3

def convert_word(word):
    result = ''
    for letter in range(len(word)):
        if letter % 2 == 0:
            result += word[letter].upper()
        else:
            result += word[letter].lower()
    return result

word = input("Enter a word: ")


converted_word = convert_word(word)
print("Converted word:", converted_word)

# 4

name = "Sandro"

if len(name) > 5:
    name = name.upper()
else:
    name = name.lower()

print(name)

# 5

full_name = ["sandro", "miqeladze"]
capitalized_names = []

for name in full_name:
    capitalized_name = name.capitalize()
    capitalized_names.append(capitalized_name)


print(capitalized_names)

# 6

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = [first_name, last_name]

capitalized_names = []

for name in full_name:
    capitalized_name = name.capitalize()
    capitalized_names.append(capitalized_name)

initials = '.'.join([name[0] for name in capitalized_names])

print(initials)

# 7

family_members = ["John", "Jane", "Jack", "Jill"]


combined_names = "-".join(family_members)

print("Family members:", combined_names)





