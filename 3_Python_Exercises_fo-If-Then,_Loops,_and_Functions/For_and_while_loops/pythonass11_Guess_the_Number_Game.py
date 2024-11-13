import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    x=0
    while x==0:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < number_to_guess:
            print("your guess is wrong, my number is higher.")
        elif guess > number_to_guess:
            print("you are wrong the number is lower.")
        else:
            print(f"{guess} is correct.")
            x=1 

guess_the_number()