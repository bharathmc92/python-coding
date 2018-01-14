#Ask the user to input the number of knights
num_knights = int(input("Enter the number of knights \n"))
day = input("Enter the day of the week \n")
print("You entered:", num_knights, "and ", day)
if num_knights < 3 or day =="Monday":
    print("Retreat!")