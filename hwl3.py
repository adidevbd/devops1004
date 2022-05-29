

## ex 1 and 2
try:
    a = 1/0
except ZeroDivisionError:
    print("please do not divide by zero ")


# ex 3

## leagel , not recommended but leagel

# ex 4 and 5
# no pyton is k sensitive so ....no exceptions can be cought

# ex 6

# ioerror is for handling user input errors
#ZeroDivisionError is to check not division by zero

# ex 7 8 9 10
coding = "utf8"
f = open("words.txt", "w", encoding=coding)
myname = input("enter your name:")
f.write(myname)
f.close()
f = open("words.txt", "r", encoding=coding)
for names in f.readlines():
    print(f"your name is {names}")

# ex 11
from PIL import Image

img = Image.open("chicken.png")

img.show()
