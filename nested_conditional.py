num_knights = int(input("Enter the number of knights \n"))
day = input("Enter the day of the week \n")
enemy = input("Enter type of enemy \n")

if enemy == "killer bunny":
    print("Holy Hand Grenade!")
else:
    #original battle rules
    if num_knights < 3 or day == "Monday":
        print("Retreat!")
    elif num_knights >= 10 and day == "Wednesday":
        print("Trojan Rabbit!")
    else:
        print("Truce?")

# print('THe shop owner said "No, no, \'e\'s uh,....he\'s resting "')
# number = "1, 2, 3, 4, 5, 6, 7, 8, 9"
# print(number[0::3])
