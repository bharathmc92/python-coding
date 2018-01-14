num_knights = int(input("Enter the number of knights \n"))
day = input("Enter the day of the week \n")

if num_knights < 3 or day == "Monday":
    print("Retreat!")
elif num_knights >=10 and day == "Wednesday":
    print("Trojan Rabbit!")
else:
    print("Truce?")