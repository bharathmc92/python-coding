# list_1 = []
# list_2 = list()
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal")
#
# print(list("The lists are equal"))
#
# another_even = sorted(even, reverse=True)
#
# print(another_even == even)
#
# another_even.sort(reverse=True)
# print(even)
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]

for number_set in numbers: #t his prints the outer list [2,4,6,8] and [1,3,5,7,9]
    print(number_set)

    for value in number_set: # this prints the values present in the list individually
        print(value)
