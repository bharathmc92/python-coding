# add to the program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal.
# You will need to set up the menu as we did in lines 5-13

menu = list()
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

# print(menu)

for meal in menu:  # meal variable is going through the individual
            # menu list and checking which list doesnt contain spam in it
    if not "spam" in meal:
        print(meal)
        for ingredients in meal:  # going through ingredients of specific lists.
            print(ingredients)
