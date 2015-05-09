import random


# This program lets two players play the game Hangman.
# Player 1 enters a secret word. Then, player 2 has seven wrong guesses before losing the game.

def getSecretWord():
    """Asks Player 1 for secret word, makes sure it is valid, and stores the word in lowercase."""
    invalid = True
    while invalid:
        secretWord = input(secretWordPrompt).strip().lower()
        if ('?' in secretWord) or ('\n' in secretWord) or ('\t' in secretWord):
            continue
        elif len(secretWord) == 0:
            continue
        else:
            invalid = False
    return secretWord

def getRandomWord():
    """Gets random word at least 6 characters long from list of common English words"""
    wordList = []
    with open('4000-most-common-english-words.csv') as file:
        for line in file:
            if len(line) > 6:
                wordList.append(line)
    wordList.pop(0)
    randomNumber = random.choice(range(len(wordList)))
    return wordList[randomNumber]


def displayHangman(wrongGuesses):
    """Display current state of Hangman based on current number of wrong guesses with a blank line on either side."""
    print()
    if wrongGuesses >= 1:
        print(' | ')
    if wrongGuesses >= 2:
        print(' 0 ')
    if wrongGuesses >= 3:
        if wrongGuesses == 3:
            print(' | ')
        elif wrongGuesses == 4:
            print('/| ')
        else:
            print('/|\\')
    if wrongGuesses >= 6:
        if wrongGuesses == 6:
            print('/  ')
        else:
            print('/ \\')
    print()
    return

def displaySecretWord(secretWord, guesses):
    """Builds string of the current state of the secret word, with unguessed characters masked as question marks"""
    length = len(secretWord)
    displayWord = ''
    for char in secretWord:
        if char.isalpha():
            if char in guesses:
                displayWord += char
            else:
                displayWord += '?'
        else:
            displayWord += char
    return displayWord

def displayPreviousGuesses(previousGuesses):
    """Displays the characters guessed so far in sorted order separated by commas"""
    print(previousGuessesPrompt, end='')
    previousGuesses.sort()
    length = len(previousGuesses)
    if length == 0:
        print()
    else:
        for i in range(length):
            if i < (length - 1):
                print(previousGuesses[i], end=', ')
            else:
                print(previousGuesses[i])
    return

def getGuess(previousGuesses):
    """Asks Player 2 for a single character guess and makes sure it is valid"""
    invalid = True
    while invalid:
        guess = input(nextGuessPrompt).strip().lower()
        if len(guess) > 1:
            print('You can only guess a single character.')
            continue
        elif len(guess) < 1:
            print('You must enter a guess.')
        elif guess in previousGuesses:
            print('You already guessed the character:', guess)
            continue
        else:
            invalid = False
    return guess



# Set-up
secretWordPrompt = 'Please enter a word or phrase to be guessed that does not contain ?: '
previousGuessesPrompt = 'So far you have guessed: '
nextGuessPrompt = 'Please enter your next guess: '
wrongGuesses = 0
guessedList = []

# ------------------------------------
# Player 1 enters secret word
# ------------------------------------

# Toggle to switch between 2 player and random word option.
# secretWord = getSecretWord()
secretWord = getRandomWord()

# Print 30 blank lines to hide word
for line in range(30):
    print()

# ------------------------------------
# Player 2 tries to guess secret word
# ------------------------------------

while wrongGuesses < 7:

    # Display current state of the game
    displayHangman(wrongGuesses)
    displayWord = displaySecretWord(secretWord, guessedList)
    print(displayWord)
    displayPreviousGuesses(guessedList)

    # Get guess from Player 2
    currentGuess = getGuess(guessedList)
    guessedList.append(currentGuess)

    # Check if Player 2 has won. If so, congratulate them and exit the loop.
    displayWord = displaySecretWord(secretWord, guessedList)
    if displayWord == secretWord:
        print('You correctly guessed the secret word:', secretWord)
        break

    # If guess is wrong, add to count.
    if currentGuess not in secretWord:
        wrongGuesses += 1

else:

    # If Player 2 gets 7 wrong guesses, they lose.

    displayHangman(wrongGuesses)
    print('You failed to guess the secret word:', secretWord)


