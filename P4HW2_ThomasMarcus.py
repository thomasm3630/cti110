#Marcus Thomas
#04/21/24
#P4HW2 
#salary


run_again = ()




name_user = input("Enter employee's name: ")

    
hours = float(input("Enter number of hours worked: "))
payrate = float(input("Enter employee's pay rate: "))
gross = hours * payrate
overtime = (hours - 40)
overtime_pay = ((overtime * 1.5) * payrate)
Regular_pay = 40 * payrate
grosspay = (overtime_pay + Regular_pay)

print()
print("Employee name:    ", name_user)
print()
print("Hours Worked  Pay Rate  OverTime     OverTime Pay   RegHour Pay   Gross Pay")
print("------------------------------------------------------------------------------")
print(hours,"        ",payrate,"    ",overtime,"        ",overtime_pay,"        $",Regular_pay,"        $",grosspay)






name_user = input("Enter employee's name or 'Done' to terminate:")
if name_user >= (a,z):
    for item in range(a,z):
        input("Enter employee's name: ")
        float(input("Enter number of hours worked: "))
        float(input("Enter employee's pay rate: "))
else:
    print("Total number of employees entered:")
    print("Total amount paid for overtime $")
    print("Total paid for regular hours: $")
    print("Total amount paid in gross: $")
