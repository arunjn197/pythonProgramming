import random

name = input("Enter Your Name: ")

print("Good Luck! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print(word)

guesses = ''
turns = 12

print("Guess the Characters")

while(turns > 0):
    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    
    if failed == 0:
        print("You win...!")
        print("The word is: ", word)
        break
    
    print()
    guess = input("Guess a character: ")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print(f'You have {turns} more guesses')

        if turns == 0:
            print("You Loose")
    
