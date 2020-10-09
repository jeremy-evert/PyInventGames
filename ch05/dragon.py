import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and you will share their treasure with you. The other dragon 
is greedy and hungry, adn will eat you on sight.''')
print()

def chooseCave():
    cave = ''
    while cave != '1' and cave !='2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! They open their jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
       print('Gives you their treasure!')
    else:
       print('That was not a dragon. It was a baboon!')

print('Program begins.')

playAgain = 'yes'

while 'yes' == playAgain or 'y' == playAgain:
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()


print('Program complete.')
