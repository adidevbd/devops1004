import random
import time

def generate_sequence(length):# - Will generate a list of random numbers between 1 to 101. The list length will be difficulty.
    MemoryList=[]
    for Num in range(1,length+1):
        MemoryList.append(str(random.randint(1,101)))
    return MemoryList


def get_list_from_user(length):# - Will return a list of numbers prompted from the user. The list length will be in the size of difficulty.
    UserMemory = []
    for Location in range(1,length+1):
        UserMemory.append(input(f"enter number in {Location} location: "))
    return UserMemory


def is_list_equal(UserList,CompList):# - A function to compare two lists if they are equal. The function will return True / False.
    if UserList == CompList:
        return True
    else:
        return False


def play(diffeclty):# - Will call the functions above and play the game. Will return True / False if the user lost or won.
    CompGeneraatedList = generate_sequence(diffeclty)
    print(CompGeneraatedList, end='')
    time.sleep(1)
    for i in range(len(str(CompGeneraatedList))):
        print("\b", end='')
    UsersList = get_list_from_user(diffeclty)
    Result = is_list_equal(CompGeneraatedList,UsersList)
    if Result == True:
        print("good job")
    else:
        print("you have failed")
