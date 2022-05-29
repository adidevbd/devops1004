# ex1
import names
import requests

allRepos = requests.get("https://api.github.com/users/avielb/repos")
mygitrepo = allRepos.json()
setRepoCount=[]
for repo in mygitrepo:
    setRepoCount.append(repo["commits_url"])
if len(setRepoCount) > 5:
    print("have enough git repos")


# ex 2


def generate_name():
    return names.get_first_name()

my_names = []
for my_range in range(1,5):
    my_names.append(generate_name())

for name in my_names:
    result = requests.get(f"https://api.agify.io/?name={name}")
    if 0< result.json()["age"]< 120:
        print("age is currect")
    else:
        print("Error age is not in range")
# e 3
import json

allUnislist = []
allUnis = requests.get("http://universities.hipolabs.com/search?country=Israel")
IlUnis = allUnis.json()
for repo in IlUnis:
    if repo["country"] == "Israel":
        allUnislist.append(repo["name"])

if len(allUnislist) >=5 :
    print("israel has more than five universities")
# ex 4
from selenium import webdriver

my_driver = webdriver.Chrome(executable_path="C:/Users/User/Downloads/chromedriver_win32/chromedriver.exe")
def testTitle(url,ExpectedTitle):

    my_driver.get(url)
    hesdElemet = my_driver.title
    if hesdElemet == ExpectedTitle:
        print("title is as expected")
    else:
        print(f"title is differ than expected\n"
              f"title is {hesdElemet}")


testTitle("https://www.ycombinator.com/","Y Combinator")

testTitle("https://hub.docker.com/", "Docker Hub Container Image Library | App Containerization")