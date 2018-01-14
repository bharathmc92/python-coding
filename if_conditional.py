print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != 5:
    if guess <5:
        print("Please guess higher number")
    else:
        print("Please guess lower number")

    guess = int(input())

    if guess ==5:
        print("Well done, you guessed it right")
    else:
        print("Sorry, you have not guessed it right")
else:
    print("You nailed it")

# if guess < 5:
#     print("Please guess higher number")
#     guess = int(input())
#     if guess == 5:
#         print("Well Done, you guessed it!")
#     else:
#         print("Sorry you have not guessed the number correctly")
# elif guess >5:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well Done, you have guessed it correctly!")
#     else:
#         print("Sorry you have not guessed it correctly")
# else:
#     print("You got it first time")