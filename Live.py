from GuessGame import GuessGame as playGessing
from MemoryGame import play as playMemory

def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).\n"
          "            Here you can find many cool games to play.")

def load_game(myname):
    try:
        gameType = int(input(f"\t\t\tplease chose your game\n"
                             f"\t\t\tenter 1 to play the gussing game\n"
                             f"\t\t\tenter 2 to play the memory game\n"
                             f"\t\t\temter 3 to play the currency rullet game\n"
                             f"\t\t\tplease enter your choice: "))
        if gameType < 1 or gameType > 3:
            print("your choice must be between 1 and 3")
            exit()

    except ValueError:
        print("your choice must be an integer between 1 and 3")
        exit()
    try:
        DeffLevel = int(input(f"please enter difficulty level between 1 and 5: "))
        if DeffLevel < 1 or DeffLevel > 5:
            print("your choice must be between 1 and 5")
            exit()
    except ValueError:
        print("your choice must be an integer between 1 and 5")
        exit()

    if gameType == 1:
        playGessing(DeffLevel,myname)
    elif gameType == 2:
        playMemory(DeffLevel)

