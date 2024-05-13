#Marcus Thomas
#4/15/2024
#P2HW1
#Input

total_exp = []


print("This program calculates and displays travel expenses")
print()
budget_bud = float(input("Enter Budget:"))
print()
location_lo = (input("Enter your travel destination:"))
print()
fuel_fu = float(input("How much do you think will spend on gas?"))
total_exp.append(fuel_fu)
print()
acc_hotel = float(input("Approximately, how much will you need for accomodation/hotel?"))
total_exp.append(acc_hotel)
print()
food_fo = float(input("Last, how much do you need for food?"))
total_exp.append(food_fo)
print("------------Travel Expenses------------")
print("Location:          ",location_lo)
print("Initial Budget:   $",budget_bud)
print("Fuel              $",fuel_fu)
print("Accomodation:     $",acc_hotel)
print("Food              $",food_fo)
print("---------------------------------------")
print()

total = sum(total_exp)
print
print("Remaining Balance:$",budget_bud - total)

