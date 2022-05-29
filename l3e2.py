# my_file = open("urls.txt")
# for line in my_file.readlines():
#     print(line)
#
from l3e1 import url_caller

def createUsersFile(my_name):
    my_file = open("names.txt", "a")
    my_file.write(f"{my_name}\n")
    my_file.close()


def readUsersFile():
    my_file = open("names.txt", "r")
    for name in my_file.readlines():
        print(f"Hello {name} ", end='')
    my_file.close()

for name in range(5):
    current_name = input("enter your name:")
    createUsersFile(current_name)

readUsersFile()
urlfile = open("urls.txt","r")

#for url in urlfile.readlines():
 #   url_caller(url)