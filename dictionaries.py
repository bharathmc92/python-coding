fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit",
         "apple": "best in michigan"}


fruit.__setitem__("strawberry","fruit in pink colour") #method to add data to the dictionary

while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print("we don't have a " + dict_key)



        # print(fruit)
        # print(fruit["apple"]) #can access individual elements by their key
        # print("############")
        # del(fruit["apple"])
        # print(fruit)
        # fruit.clear()# to clear all the entries of the fruit
        # print(fruit)
#print(fruit)

# print(fruit.__getitem__("strawberry"))

