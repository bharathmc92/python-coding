# age = int(input("How old are you?"))
# #if (age >= 16) and (age <=65):
# # if 15< age < 66:
# if (age<16) or (age>65):
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")

age = int(input("How old are you? "))
if not(age<18):
    print("You are old enough to vote")
    print("PLease put an X in the box0")
else:
    print("Please come back in {0} years".format(18-age))