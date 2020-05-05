from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
from news_reader import speak

def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    
    myHtmlData = getData('https://afswadsar.kvs.ac.in/school-announcement')
    
    # print(myHtmlData)
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(soup.preetify())
    myDatastr = ""
    for td in soup.find_all('tbody')[0].find_all('td'):
        myDatastr += td.get_text()
    myDatastr = myDatastr[1:]
    itemList = (myDatastr.split("\n\n"))
    print(myDatastr)
    speak(myDatastr)
