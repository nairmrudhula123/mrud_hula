#author:-mrudhula nair
#hangman
import random 
WORDLIST = ("phone", "laptop", "desktop", "sewer", "television", "never", "guess", "nice", "chair", "car");
WORD = random.choice(WORDLIST)
ACCEPTABLE = ("abcdefghijklmnopqrstuvwxyz")

guessed = []
state = 0
hasWon = 0
playedOnce = 0

def menu ():
    print("""
    1. Easy (9 misses)
    2. Medium (7 misses)
    3. Hard (5 misses)
    """)
    return int(input("What level do you want to play?:"))

def wantsToPlay():
    if (not playedOnce):
        return 1
    l = input("\nWould you like to play again? (y/n)")
    while (l != "y" and l != "Y" and l != "n" and l != "N"):
        l = input("\nWould you like to play again? (y/n)")
    if (l.lower() == "y"):
        return 1
    return 0

def takeNewLetter():
    global state, hasWon
    newPrint("So far, you have guessed the following letters...")
    for g in guessed:
        print(g, end=" ")
    letter = input("\n\nWhat letter would you like to guess next?\n")
    while (letter in guessed or letter not in ACCEPTABLE):
        if (len(letter) > 1):
            if (letter.lower() == WORD.lower()):
                 newPrint("You win!")
                 hasWon = 1
                 break
            else:
                newPrint("Boo... that was wrong... you're dead...")
                state = 7
                break
        else:
            if (letter not in ACCEPTABLE):
                letter = input("That character is unacceptable. You many only enter lower case letters.\n")
            else:
                letter = input("You have already guessed that letter, try another one...\n")
    guessed.append(letter)
    if (letter not in WORD):
        state += 1
    return

def drawWord():
    tempWord = ""
    for c in WORD:
        if (c in guessed):
            tempWord += c + " "
        else:
            tempWord += "_ "
    newPrint(tempWord)
    return

def drawStickman():
    if (state >= 7):
        print("   _______")
        print("|/      |")
        print("|      (_)")
        print("|      \|/")
        print("|       |")
        print("|      / \\")
        print("|")
        print("|___")
        print("Oops. You're dead.")
    elif (state == 6):
        print("   _______")
        print("|/      |")
        print("|      (_)")
        print("|      \|/")
        print("|       |")
        print("|      / ")
        print("|")
        print("|___")
    elif (state == 5):
        print("   _______")
        print("|/      |")
        print("|      (_)")
        print("|      \|/")
        print("|       |")
        print("|")
        print("|")
        print("|___")
    elif (state == 4):
        print("   _______")
        print("|/      |")
        print("|      (_)")
        print("|      \|/")
        print("|")
        print("|")
        print("|")
        print("|___")
    elif (state == 3):
        print("   _______")
        print("|/      |")
        print("|      (_)")
        print("|      \|")
        print("|")
        print("|")
        print("|")
        print("|___")
    elif (state == 2):
        print("   _______")
        print("|/      |")
        print("|      (_)")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|___")
    elif (state == 2):
        print("   _______")
        print("|/      |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|___")
    elif (state == 1):
        newPrint("As this is your first mistake, I will let you off...")
        print("   _______")
        print("|/")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|___")
    elif (state == 0):
        print("   _______")
        print("|/")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|___")

def hasGuessed():
    if (hasWon == 1):
        return 1
    if (state >= 7):
        return 1
    for c in WORD:
        if (c not in guessed):
            return 0
    if (len(guessed) == 0):
        return 0
    return 1

def setup_game():
    newPrint("Welcome to the Hangman game!")
    newPrint("I have chosen a random word from my super secret list, try to guess it before your stickman dies!")

def newPrint(message, both = 1):
    msg = "\n" + message
    if (both != 1):
        msg += "\n"
    print(msg)

def main():
    global guessed, hasWon, state, playedOnce, WORD, WORDLIST
    setup_game()
    newPrint("My word is " + str(len(WORD)) + " letters long.")
    while (wantsToPlay() == 1):
        WORD = random.choice(WORDLIST)
        guessed = []
        playedOnce = 1
        hasWon = 0
        state = 0
        while (hasGuessed() == 0 and state < 7):
            drawStickman()
            drawWord()
            takeNewLetter()
        drawStickman()
        newPrint("My word was " + WORD)

main()
