

# import requests
#
# requests.get("ht5p://www.google.com")
#

try:
    a = int(input("enter first number:"))
    b = int(input("enter second number:"))
    print(a/b)
    r = open("dddd")
except ZeroDivisionError:
    print("could not divide by zero")
except FileNotFoundError:
    print("could not find file")
except Exception as  e:
    print(e.args)
print("skjhdfkjh")
