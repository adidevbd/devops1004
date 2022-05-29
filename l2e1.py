isTrue = False
a = 2
b = 2
strOne = "One"
strThree = "Three"
c = [1, 2, 3]
d = [1, 2, 3]
if a == b:
    print("a equals b")
if c == d:
    print("c equals d")
if a is b:
    print("a is b")
if c is d :
    print("c is d")
if a < b :
    print("a is less than b")
elif a == b:
    print("a is equal to b")
elif strOne != strThree:
    print("bla")
age = int(input("enter your age:"))
if 0 < age < 120:
    print("ok")
my_names = ["adi", "ben", "noam","arthur", "ron"]
my_list = []
if "zohar" in my_list:
    print("found it")
else:
    print("zohar not found")