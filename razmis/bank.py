import random

accounts = {}

def bank():

    def display_menu():
        user_choice = int(input("Do you wish to enter the bank? (1- Yes, 5 - No): "))
        
        while user_choice != 5:
            user_choice = int(input("Welcome, what do you wish to do? You have a few options. Create an Account, Deposit Funds, Withdraw Funds, Check Balance or Exit the Program. Which one do you choose 1-5?: "))

            if user_choice == 1:
                name = input("What's your name? ")
                generated_num = random.randint(100000, 999999)
                print("Your account number will be:", generated_num)
                accounts[generated_num] = 0
            elif user_choice == 2:
                checking_acc_num = int(input("What's your account number? "))
                if checking_acc_num in accounts:
                    deposit_amount = int(input("How much do you want to deposit? "))
                    accounts[checking_acc_num] += deposit_amount
                else:
                    print("Account not found.")
            elif user_choice == 3:
                checking_acc_num = int(input("What's your account number? "))
                if checking_acc_num in accounts:
                    withdrawal_amount = int(input("How much do you want to withdraw? "))
                    if accounts[checking_acc_num] >= withdrawal_amount:
                        accounts[checking_acc_num] -= withdrawal_amount
                    else:
                        print("Insufficient funds.")
                else:
                    print("Account not found.")
            elif user_choice == 4:
                checking_acc_num = int(input("What's your account number? "))
                if checking_acc_num in accounts:
                    print("Your account balance is:", accounts[checking_acc_num])
                else:
                    print("Account not found.")
            elif user_choice == 5:
                print("Goodbye")
            else:
                print("Error, try again.")

    display_menu()


bank()





