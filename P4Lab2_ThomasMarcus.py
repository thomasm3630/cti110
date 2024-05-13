#Marcus Thomas
#04/28/2024
#p4_Lab2
#Loop

run_again = 'yes'

while run_again != "no":

    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")

    else:
         print("This program does not handle negatives values")

    run_again = input("Would you like to run the program again? ")
print("program is ending....")
