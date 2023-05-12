def HangMan(incorrectGuesses):
    if incorrectGuesses == 1:
        for each in range(0, 6):
            print("                    ")
        print("          __________")
    elif incorrectGuesses == 2:
        for each in range(0, 6):
            print("                   |")
        print("          __________")
    elif incorrectGuesses == 3:
        print("          __________")
        for each in range(0, 6):
            print("                   |")
        print("          __________")
    elif incorrectGuesses == 4:
        print("          __________")
        print("           |       |")
        print("           |       |")
        print("                   |")
        print("                   |")
        print("                   |")
        print("                   |")
        print("          __________")
    elif incorrectGuesses == 5:
        print("          __________")
        print("           |       |")
        print("           |       |")
        print("           O       |")
        print("                   |")
        print("                   |")
        print("                   |")
        print("          __________")
    elif incorrectGuesses == 6:
        print("          __________")
        print("           |       |")
        print("           |       |")
        print("           O       |")
        print("          /|\      |")
        print("                   |")
        print("                   |")
        print("          __________")
    elif incorrectGuesses == 7:
        print("          __________")
        print("           |       |")
        print("           |       |")
        print("           O       |")
        print("          /|\      |")
        print("          / \      |")
        print("                   |")
        print("          __________")