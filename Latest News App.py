import requests
import json
import time

def read(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice").Speak

    speak(str)


read("Hello To All ")

time.sleep(2)
# Steps To Find any News API
# #
# 1. go to chrome search for news API
# 2. create new account and get your api key
# 3. then go to source section search your favorite News API
# 4. copy that url
# 5. then enter here

while(True):
    read("enter your choice which type of news do you want to listen ")
    read("enter 1 for health news in india")
    read("enter 2 for bussiness news in india")
    read("enter 3 for sport news in india")
    read("enter 4 for technology news in india")
    read("enter your choice i am waiting for your interest of news ")
    n = int(input("enter your choice : "))
    if (n == 1):
        str ="https://newsapi.org/v2/top-headlines?country=in&category=healt" \
             "h&apiKey=3982dbaaa1d84cacba10d3c020c6d033"
        read("latest health news are ....")
        break
    elif (n == 2):
        str ="https://newsapi.org/v2/top-headlines?country=in&category=busine" \
             "ss&apiKey=3982dbaaa1d84cacba10d3c020c6d033"
        read("latest bussiness news are....")
        break
    elif (n == 3):
        str ="https://newsapi.org/v2/top-headlines?country=in&category=sports&" \
             "apiKey=3982dbaaa1d84cacba10d3c020c6d033"
        read("latest sport news are....")
        break
    elif(n==4):
        str="https://newsapi.org/v2/top-headlines?country=in&category=technology" \
            "&apiKey=3982dbaaa1d84cacba10d3c020c6d033"
        read("latest technology news are....")
        break
    else:
        print("enter correct choice")



# example for API
# str="https://newsapi.org/v2/top-headlines?country=in&apiKey=3982dbaaa1d84cacba10d3c020c6d033"

if __name__== '__main__':
    url=str
    news=requests.get(url).text
    news_dict=json.loads(news)
    art=news_dict['articles']
    for article in art:
        read(article['title'])
        time.sleep(2)
        read("Moving on to the next news...Listen Carefully")
        time.sleep(3)

    read("Thanks for listening")

