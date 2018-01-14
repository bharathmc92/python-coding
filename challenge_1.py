#program to check the age of a person and allow if he is eligible for 18-30 holiday
name = input("Enter your Name:")
age = int(input("Enter your age: "))
if 17 < age < 31:
    print("Welcome to the Holiday {0}".format(name))
else:
    print("Sorry, you are not eligible for this holiday trip {0}".format(name))