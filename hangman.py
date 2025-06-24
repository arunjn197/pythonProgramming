import random
from collections import Counter

somefruits = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

fruits = somefruits.split(' ')

fruit = random.choice(fruits)

print(fruit)
if __name__ == '__main__':
    print('Guess the fruit! HINT: fruit is a name of a fruit')
    for i in fruit:
        # For printing the empty spaces for letters of the fruit
        print('_', end=' ')
    print()

    playing = True
    # List for storing the letters guessed by the player
    letterGuessed = ''
    chances = len(fruit) + 2
    correct = 0
    flag = 0

    try:
        while (chances != 0) and flag == 0:  # Flag is updated when the fruit is correctly guessed
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            # If letter is guessed correctly
            if guess in fruit:
                # k stores the number of times the guessed letter occurs in the fruit
                k = fruit.count(guess)
                for _ in range(k):
                    letterGuessed += guess  # The guessed letter is added as many times as it occurs

            # Print the fruit
            for char in fruit:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(fruit)):
                    print(char, end=' ')
                    correct += 1
                # If user has guessed all the letters
                # Once the correct fruit is guessed fully,
                elif (Counter(letterGuessed) == Counter(fruit)):
                    # the game ends, even if chances remain
                    print("The fruit is: ", end=' ')
                    print(fruit)
                    flag = 1
                    print('Congratulations, You won!')
                    break  # To break out of the for loop
                    break  # To break out of the while loop
                else:
                    print('_', end=' ')

        # If user has used all of his chances
        if chances <= 0 and (Counter(letterGuessed) != Counter(fruit)):
            print()
            print('You lost! Try again..')
            print('The fruit was {}'.format(fruit))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()