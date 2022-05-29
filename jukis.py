import random
import time


def mg():
    diffculty = 2


def generate_sequence(length):# - Will generate a list of random numbers between 1 to 101. The list length will be difficulty.
    MemoryList=[]
    for Num in range(1,length+1):
        MemoryList.append(random.randint(1,101))
    return MemoryList

compList = generate_sequence(3)
print(compList, end='')
time.sleep(1)
for i in range(len(str(compList))):
    print("\b",end='')