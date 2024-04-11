name = input("What's your name?: ")

password = input("What do you want your password to be?: ")

repeat_password = input("Repeat the password: ")

if repeat_password != password:
  print("The repeated password is incorrect.")
else:
  print("You passed the registration")