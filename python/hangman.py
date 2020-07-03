import random
HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 0   |
     |
     |
    ===''','''
 +---+
 0   |
 |   |
     |
    ===''','''
 +---+
 0   |
/|   |
     |
    ===''','''
 +---+
 0   |
/|\  |
     |
    ===''','''
 +---+
 0   |
/|\  |
/    |
    ===''','''
 +---+
 0   |
/|\  |
/ \  |
    ==='''
    ]
words = 'administrative region adding that pulling human rights into this is just'.split()

def getRandomWord(wordList):
    wordIndex = random.randint(0,len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedletters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedletters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedletters:
        print(letter, end='')
    print()
    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = str(guess).lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)

    if str(guess) in secretWord:
        correctLetters = correctLetters + str(guess)

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "'+ secreWord + '"!You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + str(guess)
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!')
            print('After' + str(len(missedLetters)) + ' missed guessed and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)
            gameIsDone = False
        else:
            break
        
            
            
