change = float(input("Enter an amount of money: $"))

print(f"Change Amount: {change}")

change = round(change *100)

print(f"Change Amount: {change}")

num_dollars = change // 100
change = change - (num_dollars * 100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickels = change // 5
change = change - (num_nickels * 5)

num_pennies = change

if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollar")

if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} Quarters")
    else:
        print(f"{num_quarters} Quarters")

if num_dimes > 0:
    if num_quarters == 1:
        print(f"{num_dimes} Dime")
    else:
        print(f"{num_dimes} Dimes")
if num_nickels > 0:
    if num_nickels == 1:
        print(f"{num_nickels} Nickels")
    else:
        print(f"{num_nickels} Nickels")

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Pennies")
    else:
        print(f"{num_pennies} Pennies")
