# This is our gess the number game
import random
print('start program')

guessesTaken = 0
guessesAllowed = 6

print('Hello! How should I address you?')
myName = input()

number = random.randint(1,20)
print('Hello, ' 
+ myName + ', I am thinking of a number between 1 and 20.')

for guessesTaken in range(guessesAllowed):
    print('Please guess a number.')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('That guess was lower than what I am thinking about')

    if guess > number:
        print('That guess was higher than what I am thinking about')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Well done, '
    + myName + '! You guessed my number in '
    + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('I am sorry, ' + myName + ', the number was '
    + number + '.')




print('end program')

