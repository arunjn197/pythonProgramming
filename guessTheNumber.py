"""
Number Guessing Game:
User will enter the upper and lower bound.
System will select the Random Number
User will have 7 Chances to Guess the Number selected by System
"""
import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

low  = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

totalChance = 7
guessedChance = 0
selectedNumber = random.randint(low, high)

while guessedChance < totalChance:
    inputNumber = int(input("Enter the Number: "))
    guessedChance += 1
    if inputNumber == selectedNumber:
        print(f'Correct! The number is {selectedNumber}. You guessed it in {guessedChance} attempts.')
        break
    
    elif guessedChance >= totalChance and inputNumber != selectedNumber:
        print(f'Sorry! The number was {selectedNumber}. Better luck next time.')
    
    elif inputNumber > selectedNumber:
        print('Too high! Try a lower number.')
    
    elif inputNumber < selectedNumber:
        print('Too low! Try a higher number.')