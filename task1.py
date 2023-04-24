#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
import random
num = random.randint(1, 100)

for i in range(10):
    guess = int(input("Enter your number"))
    if guess == num:
        i += 1
        print(f"You did it in {i} guesses!")
        exit()
    elif guess > num:
        print("Lower")
    elif guess < num:
        print("Higher")
print("You lose :(")