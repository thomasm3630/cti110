#Marcus Thomas
#05/07/2024
#P5H1



print("Welcome to Math Quiz")
print()
print()
print("MAIN MENU")
print("-------------------")
print("1. Adding Random Numbers")
print("2. Subtracting Random Numbers")
print("3. Exit")
print()
menu_option = int(input("Please choose one of the menu option :"))

import random
low = 1
high = 100
number = random.randint(low,high)
number_2 = random.randint(low,high)
number_3 = random.randint(low,high)
number_4 = random.randint(low,high)
while menu_option != 4:
    if menu_option == 1:
        print(number)
        print("+", number_2)
        answer_p = int(input("Enter answer :"))


            
    elif menu_option == 2:
        print(number_3)
        print("-", number_4)
        input("Enter answer :")
    elif menu_option == 3:
        print("Thank you for playing ...")
        print("Bye")
    else:
        print("You chose an invalid option")

print()
