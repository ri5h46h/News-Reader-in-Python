from bs4 import BeautifulSoup
import requests
import csv

def getData(url):
    r = requests.get(url)
    return r.text

def speak(str):
    from win32com.client import Dispatch 
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == "__main__":

    myHtmlData= getData('https://www.hindustantimes.com/india-news/')

    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(soup.prettify())

    
    for a in soup.find("div" ,{'class': 'news-area more-news-section'}).find_all('a'):
        print(a.get_text())
        speak(a.get_text())
