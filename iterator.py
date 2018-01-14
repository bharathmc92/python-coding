list_countries = ["India", "United States", "Canada", "Australia", "Japan"]
my_iterator = iter(list_countries)

for i in range(0, len(list_countries)):
     indi_countries = next(my_iterator)
     print(indi_countries)