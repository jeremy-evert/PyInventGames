import random
Gallows_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''',  '''
  +---+
  O   |
  |   |
      |
     ===''',  '''
  +---+
  O   |
 /|   |
      |
     ===''',  '''
  +---+
  O   |
 /|\  |
      |
     ===''',  '''
  +---+
  O   |
 /|\  |
 /    |
     ===''',  '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    # This function returns a random string from 
    # the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(Gallows_PICS[(len(missedLetters))])

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blands[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: 
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter only.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Please choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER!')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswitch('y')

def printGreeting():
    print(Gallows_PICS[6], '*_\|*_G_A_L_L_O_W_S_*|/_*')

print('begin program.')
printGreeting()
middedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
         correctLetters = correctLetters + guess

        foundAllLetters = Ture
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLEtters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print('Yes! The secret word is "' + secretWord + '"! You have won!')
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess



print('program complete')
