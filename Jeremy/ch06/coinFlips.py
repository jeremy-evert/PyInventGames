import random

def printGreeting():
    print('''I will flip a coin 1,000 times.
Guess how many times it will come up heads.
(Press enter to begin)''')

def flipTheCoins():
    flips = 0
    heads = 0
    while 1000 > flips:
        if 1 == random.randint(0,1):
            heads += 1
        flips += 1

        if 900 == flips:
            print('900 flips and there have been ' + str(heads) + ' heads.')

        if 100 == flips:
            print('At 100 tosses, heads has come up ' + str(heads) +
                  ' times so far.')

        if 500 == flips:
            print('Halfway done, and heads has come up ' + str(heads) +
                  ' times.')

    return heads

def displayResults(guess, actual):
    if(userGuess == heads):
        print('Spot on')
    if(userGuess > heads):
        print('you were too high.')
    if(userGuess < heads):
        print('you were too low.')
    print('out of 1,000 coin tosses, heads came up ' + str(heads) + ' times!')

print('Program begins.')

printGreeting()
userGuess = input('Please enter your guess.')
userGuess = int(userGuess)

heads = flipTheCoins()
print()

displayResults(userGuess, heads)

print('Program Complete')


