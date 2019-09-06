from bs4 import BeautifulSoup
import requests
import json


# this file will be used for actually manipulating and using the data
with open('twitterData.json') as json_file:
    jsonData = json.load(json_file)

for i in jsonData:
    print i['date'] # print all the dates for each tweet

for i in jsonData:
    if "obama" in i['tweet'].lower():
        print i #prints each tweet if obama has been found
