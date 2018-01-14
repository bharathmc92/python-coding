# for i in range(10):
#     print("i is now {}".format(i))
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1
# available_exits = ["east", "north east", "south"]
#
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit == "quit":
#         print("Game Over")
#         break
#
# else:
#     print("aren't you glad you got out of there!")

#write a program to limit the execution to 5 times
import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())
no_times = 0
while no_times < 4:
    if guess == 0:
        print("You have exited the game")
        break
    if guess != answer:
        if guess < answer:
            print("Please guess higher or Press 0 to exit the game")
            no_times += 1
            guess = int(input())

        elif guess > answer:  # guess must be greater than number
            print("Please guess lower or Press 0 to exit the game")
            no_times += 1
            guess = int(input())

    else:
        print("Well done, you guessed it")
        break
else:
     print("Sorry, you have not guessed correctly")