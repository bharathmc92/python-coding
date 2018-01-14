# for i in range(1,20):
#     print("i is now {0}".format(i))
#
# #to print individual numbers
# number = "9,223,372,036,854,775,807"
# for i in range(0, len(number)):
#     print(number[i])

#to print only numbers and skip commas
# number = "9,223,372,036,854,775,807"
# for i in range(0, len(number)):
#     if number[i] in "0123456789":
#         print(number[i],end='')

#to print the numbers and skip commas
#alternative method-> converting string to integer
number = "9,223,372,036,854,775,807"
cleanedNumber = ''
for i in range(0, len(number)):
     if number[i] in "0123456789":
            cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print("THe number is {}".format(newNumber))
