import random


def get_guess_from_user(PlayerName,diffeclty):
    print(f"hello {PlayerName} and welcome to the gussing game")
    try:
        userNumber = int(input(f"pleas enter a number between 1 and {diffeclty} :"))
    except ValueError:
        print(f"your choice must be an integer between 1 and {diffeclty}")
        exit()
    return userNumber


def generate_number(diffeclty):
    return random.randint(1, diffeclty)


def compare_results(userNumber, CompChoice):
    print(f"userNumber {userNumber}")
    print(f"CompChoice {CompChoice}")
    if userNumber == CompChoice:
        return True
    else:
        return False

def play(userNumber,CompChoice):
    Result = compare_results(userNumber,CompChoice)
    if Result == True:
        print("wi pi you gusset the number ")
    else:
        print("you were not able to guss the number "
              " better luck next time"
              f"the number was {CompChoice}")

def GuessGame(diffeclty,PlayerName):
    CompNumbers = generate_number(diffeclty)
    UserNumbers = get_guess_from_user(PlayerName,diffeclty)
    play(UserNumbers, CompNumbers)


# GuessGame(4, "alona")