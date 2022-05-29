## l 2 e A

X = 6
Y = 7
if X > Y:
    print("BIG")
elif X < Y:
    print("small")

## hw l 2 e B
for iteration in range(5):
    print(f"in iteration number {iteration +1}")

## l 2 e C

my_array = [1, 2, 3, 4]

for array in my_array:
    if array == 1:
        print("summer")
    elif array == 2:
        print("winter")
    elif array == 3 :
        print("fall")
    elif array == 4:
        print("spring")

# l2 e D

## the loop will run 10 times the last thing that will be printed is the number 10

# l2 e E

age = 46
firstLetter = "a"
StoD = 0.3
DidFlew = True
appNumbur = 30
print(f"my age is {age} , the first letter of my last name is {firstLetter}\nshekel to dolar currency now is {StoD}")
if DidFlew:
    print("I flew abroad")
else:
    print("I did not flew abroad")
print(f"my appartment number is {appNumbur}")
AplusStoD = age + StoD
print(AplusStoD)

## l 2 e F

phoneNumber = input("enter your phone number:")
print(f"the phone number you enterd is {phoneNumber}")

## l 2 e G

def printHello():
    print("hello")

def calculate():
    sum = 5 + 3.2
    print(sum)

# printHello()
# calculate()

# l 2 e H

def printMyName(fname):
    print(f"user enterd {fname} as his name")

def divbytwo(yournumber):
    if type(yournumber) is int:
        result = yournumber / 2
        print(f"the result dividing your number by 2 is {result}")
    else:
        print("you did not enter a number")
divbytwo("ddd")
divbytwo(9)


## l 2 e I

def my_sum(first, second):
    if type(first) is not int or type(second) is not int:
        print("one of you params is not an integer pleas check and re enter params")
    else:
        return first + second
print(f"the sum of my numbers is {my_sum(4,3)}")

def concutStirngs(sone, stwo):
    if type(sone) is not str or type(stwo) is not str:
        print("pleas enter two valis strings")
    else:
        return sone + " " + stwo

print(concutStirngs("test", "one"))

# l 2 e K


def printpiramid(psize):
    if type(psize) is not int:
        print("pleas enter valid integer")
        return
    for i in range(psize+1):
        for mprint in range(i):
            print("#" , end ="")
        print("")
printpiramid(8)

# l2 e l


def DrewEx(Exsize):
    for location in range(Exsize):
        for mynewrange in range(location+1):
            if mynewrange == location or Exsize - location - 1 == mynewrange:
                print("#", end='')
            else:
                print(" ", end='')
        else:
            for fill in reversed(range(Exsize-location-1)):
                if Exsize - mynewrange == Exsize-fill:
                    print("#", end='')
                else:
                    print(" ", end='')
        print()

DrewEx(7)
