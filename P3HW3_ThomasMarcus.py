#Marcus Thomas
#04/21/24
#P3HW2 
#salary

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
payrate = float(input("Enter employee's pay rate: "))
gross = hours * payrate
overtime = (hours - 40)
overtime_pay = ((overtime * 1.5) * payrate)
Regular_pay = 40 * payrate
grosspay = (overtime_pay + Regular_pay)

print()
print("Employee name:    ", name)
print()
print("Hours Worked     Pay Rate     OverTime     OverTime Pay        RegHour Pay     Gross Pay")
print("-------------------------------------------------------------------------------------------------")
print(hours,"            ",payrate,"        ",overtime,"      ",overtime_pay,"              ",Regular_pay,"          ",grosspay)
