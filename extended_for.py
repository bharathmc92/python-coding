for state in {"not pinin","no more","a stiff","berfit of life"}:
    print("This parrot is "+state) # this is known as concatination. I
    #it can be used only for string data type
    #print("This parrot is {}".format(state)) #alternative to the above statement

for i in range (0,100,5): #here 5 is known as step function
    print("i is {}".format(i))

#tables
for i in range (1,15):
    for j in range (1,11):
        print("{0} * {1} = {2}".format(i, j , (i*j)))#0,1,2 must be numbered correctly
    print("==================")