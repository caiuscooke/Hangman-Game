# hangman game coaches guide

# things they will learn in this lesson:
# how to import libraries
# how to use lists and:
#   indexing
#   declaring empty lists
#   appending to lists
#   .join lists
#   iterating over lists with for loops
#   replacing list and string items using index
# how to use while loops
# how to use for loops
# how to use break
# how to use not in and in keywords
# how to use != operator

import random # needed to use the randint function
from HangmanBoardPrint  import HangMan  # file to store printing out the incorrect guesses board function

print("Welcome to Hangman!")

randomWordList = ["cheese", "food", "putt", "engineering", "forceful"] # use a list to store the random words
randomWord = randomWordList[random.randint(0, len(randomWordList) - 1)] # get a random word by using the randint function in the index of a list, set that to a variable

gameBoard = [] # declare an empty list, which will be used to print underscores as the game board

gameOver = False

for eachLetter in randomWord:
    gameBoard.append("_") # fills the gameBoard list with the number of hyphens needed to 

print('Type a letter to make a guess. If you ever would like to give up, simply type "exit"')

print("".join(gameBoard)) # prints the gameboard before the first user input. This function works by finding the items in the list and joining them with a seperator denoted with the quotes

userInput = input() # gets the user input before the loop in order to be able to skip the loop if necessary
incorrectGuesses = 0
incorrectlyGuessedLetter = []

while gameOver == False: # uses a bool variable to check if the game should keep running or not
    
    if userInput != "exit": # if the user does NOT enter exit, check their guess with each letter

        if userInput not in randomWord:
            print("That letter is not in the word!")
            incorrectGuesses += 1

            if userInput not in incorrectlyGuessedLetter:
                incorrectlyGuessedLetter.append(userInput)
            else:
                print("You already guessed that letter!")

        else:
            print("You got one!")
            
            for eachLetter in range(len(randomWord)): # uses a range of numbers due to the first-found nature of using index and replace functions
            
                if userInput == randomWord[eachLetter]: # if the user's guess matches the letter at the index given by the for loop
                    gameBoard[eachLetter] = userInput # replace the _ at the same spot on the game board with the letter guessed
        
        HangMan(incorrectGuesses)
        print("".join(gameBoard))
    else:
        break # if the user does input "exit", break the while loop
    
    if incorrectGuesses == 7:
        print("Game Over! Better luck next time.")
        break

    if "_" not in gameBoard: # right after the loop, if the game board has no hyphens in it that means they won
        gameOver = True
    else:
        print(" ".join(incorrectlyGuessedLetter))
        print(7 - incorrectGuesses, " wrong guesses left!")
        userInput = input() # they didn't win, so get user input again until they do or lose

if gameOver == True: # if the user breaks the game loop by gameOver being true, print congrats, otherwise print a goodbye message
    print("Congratulations! You win!")
elif gameOver == False and incorrectGuesses != 7:
    print("Sorry to see you go!")