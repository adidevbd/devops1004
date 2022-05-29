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