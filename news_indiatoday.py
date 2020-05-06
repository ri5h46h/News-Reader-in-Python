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
    
    myHtmlData= getData('https://www.indiatoday.in/india')

    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(soup.prettify())

    
    for h2 in soup.find("div" ,{'class': 'view-content'}).find_all('h2'):
        print(h2.get_text())
        speak(h2.get_text())
        



    









