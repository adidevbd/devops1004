from datetime import datetime
import requests

def url_caller(url):
    respons = requests.get(url)
    if respons.status_code == 200 :
        print(f"{url} is ok")

#
# for url in [ "http://github.com",
#              "https://google.com",
#              "https://david.com"]:
#     url_caller(url)
# print(datetime.now())
