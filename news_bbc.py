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
    
    myHtmlData= getData('https://www.bbc.com/news/world/asia/india')
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(soup.prettify())

    
    for h3 in soup.find("div" ,{'class': 'gel-layout gel-layout--equal'}).find_all('h3'):
        print(h3.get_text())
        speak(h3.get_text())
