def nearsetMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

def lostMessage():
    print ("\n\nYOU LOSE !")
    print("Better luck next time !")
    exit(0)

def checkConsecutive(numbers):
    i = 1

    while i < len(numbers):
        if(numbers[i] - numbers[i - 1] != 1):
            return False
        i += 1

    return True

def startGame():
    numbers = []
    last = 0

    while True:
        print ("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input("> ")

        if chance == "F":
            while True:
                if last == 20:
                    lostMessage()
                else:
                    print ("\nYour Turn.")
                    print ("\nHow many numbers do you wish to enter?")
                    inputNumbers = int(input("> "))

                    if inputNumbers > 0 and inputNumbers <= 3:
                        comp = 4 - inputNumbers
                    else:
                        print ("Wrong input. You are disqualified from the game.")
                        lostMessage()
                
                i, j = 1, 1
                print ("Now enter the values")
                while i <= inputNumbers:
                    a = input('> ')
                    a = int(a)
                    numbers.append(a)
                    i = i + 1

                last = numbers[-1]

                if checkConsecutive(numbers) == True:
                    if last == 21:
                        lostMessage()
                    else:
                        #"Computer's turn."
                        while j <= comp:
                            numbers.append(last + j)
                            j = j + 1
                        print ("Order of inputs after computer's turn is: ")
                        print (numbers)
                        last = numbers[-1]
                else:
                    print ("\nYou did not input consecutive integers.")
                    lostMessage()
        elif chance == "S":
            comp = 1
            last = 0
            while last < 20:
                #"Computer's turn"
                j = 1
                while j <= comp:
                    numbers.append(last + j)
                    j = j + 1
                print ("Order of inputs after computer's turn is:")
                print (numbers)
                if numbers[-1] == 20:
                    lostMessage()
                    
                else:
                    print ("\nYour turn.")
                    print ("\nHow many numbers do you wish to enter?")
                    inp = input('> ')
                    inp = int(inp)
                    i = 1
                    print ("Enter your values")
                    while i <= inp:
                        numbers.append(int(input('> ')))
                        i = i + 1
                    last = numbers[-1]
                    if check(numbers) == True:
                        # print (numbers)
                        near = nearestMultiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        # if inputs are not consecutive
                        # automatically disqualified
                        print ("\nYou did not input consecutive integers.")
                        # print ("You are disqualified from the game.")
                        lostMessage()
            print ("\n\nCONGRATULATIONS !!!")
            print ("YOU WON !")
            exit(0)
            
        else:
            print ("wrong choice")


game = True    
while game == True:
        print ("Player 2 is Computer.")
        print("Do you want to play the 21 number game? (Yes / No)")
        ans = input('> ')
        if ans =='Yes':
            startGame()
        else:
            print ("Do you want quit the game?(yes / no)")
            nex = input('> ')
            if nex == "yes":
                print ("You are quitting the game...")
                exit(0)
            elif nex == "no":
                print ("Continuing...")
            else:
                print ("Wrong choice")