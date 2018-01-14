parrot_list = ["non pinin","no more","a stiff", "breft of life"]

parrot_list.append("A Norwegian Blue")

for state in parrot_list:
    print("This parrot is {}".format(state))

even = [0, 2, 4 , 6, 8] #this is also list
odd = [1, 3, 5, 7, 9] #this is also list

numbers = even + odd #numbers is the third list
numbers_in_order = sorted(numbers)
print(numbers_in_order)

if numbers == numbers_in_order:
    print("The lists are equal")
else:
    print("The lists are not equal")

if numbers_in_order == sorted(numbers):
    print("The lists are equal")
else:
    print("The lists are not equal")
