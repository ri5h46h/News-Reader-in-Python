# This Python Program will show news from various famous news sources like ndtv,
# Hindustan Times, IndiaToday and more...
# Program by Rishabh Narayan

# importing the modules
import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install bs4
import csv
import json
import pyttsx
engine = pyttsx.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 130)
# engine.say("Hello, I can speak anything ...")
engine.runAndWait()

def speak(str):
    engine.say(str)
    engine.runAndWait()




# Defining main functions of the program
def getData(url):
    '''This getData function will fetch the HTML Data from the
    URL passed as argument'''
    r = requests.get(url)
    return r.text


def speak1(str):
    '''This speak function will speak the news headlines which are
    retrieved from the URL'''
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


print(
    "\n-------------- Welcome to News reader designed in Python. -------------- \n -------------- Made with love ❤ by Rishabh Narayan -------------- ")


# speak("My name is Rishabh Narayan")  # check

# from here I am defining the functions for news sources

def mainProgram():
    def newsIndianExpress():
        myHtmlData = getData('https://indianexpress.com/section/india/')
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())

        for a in soup.find("div", {'class': 'nation'}).find_all('a'):
            print(a.get_text())
            speak(a.get_text())

    # newsIndianExpress()

    def newsBBC():
        myHtmlData = getData('https://www.bbc.com/news/world/asia/india')
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())

        for h3 in soup.find("div", {'class': 'gel-layout gel-layout--equal'}).find_all('h3'):
            print(h3.get_text())
            speak(h3.get_text())

    # newsBBC()

    def newsEconomicTimes():
        myHtmlData = getData('https://economictimes.indiatimes.com/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())

        for a in soup.find("div", {'class': 'tabsContent'}).find_all('a'):
            print(a.get_text())
            speak(a.get_text())

    # newsEconomicTimes()

    def newsHindustanTimes():
        myHtmlData = getData('https://www.hindustantimes.com/india-news/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())

        for a in soup.find("div", {'class': 'news-area more-news-section'}).find_all('a'):
            print(a.get_text())
            speak(a.get_text())

    # newsHindustanTimes()

    def newsIndiaToday():
        myHtmlData = getData('https://www.indiatoday.in/india')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())

        for h2 in soup.find("div", {'class': 'view-content'}).find_all('h2'):
            print(h2.get_text())
            speak(h2.get_text())

    # newsIndiaToday()

    def newsNDTV():
        myHtmlData = getData('https://www.ndtv.com/india?pfrom=home-mainnavgation')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())

        for a in soup.find("div", {'class': 'new_storylising'}).find_all('a'):
            print(a.get_text())
            speak(a.get_text())

    # newsNDTV()

    def news_news18():
        myHtmlData = getData('https://www.news18.com/india/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())

        for a in soup.find("div", {'class': 'section-blog'}).find_all('a'):
            print(a.get_text())
            speak(a.get_text())

    # news_news18()

    def newsAPI():
        url = ('http://newsapi.org/v2/top-headlines?country=in&apiKey=a5b172a2897744d9af10f51fa659197e')

        response = requests.get(url)
        text = response.text
        my_json = json.loads(text)
        x = int(input("Enter the number of headlins you want to see : "))
        for i in range(0, x):
            speak(my_json['articles'][i]['title'])
            print(my_json['articles'][i]['title'])

    # newsAPI()

    def newsTOI():
        myHtmlData = getData('https://timesofindia.indiatimes.com/india')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())

        for a in soup.find("div", {'class': 'main-content'}).find_all('a'):
            print(a.get_text())
            speak(a.get_text())

    # newsTOI()

    def techNewsIndiaToday():
        myHtmlData = getData('https://www.indiatoday.in/technology')
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())

        for a in soup.find("div", {'class': 'itg-layout-container itg-front tech-layout-page'}).find_all('a'):
            print(a.get_text())
            speak(a.get_text())

    # techNewsIndiaToday()

    def techNewsGadgets360():
        myHtmlData = getData('https://gadgets.ndtv.com/news')
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())

        for a in soup.find("div", {'class': 'content_section'}).find_all('a'):
            print(a.get_text())
            speak(a.get_text())

    # techNewsGadgets360()

    def sportsIndianExpress():
        myHtmlData = getData('https://indianexpress.com/section/sports/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())

        for a in soup.find("div", {'class': 'nation'}).find_all('a'):
            print(a.get_text())
            speak(a.get_text())

    def googleNews():
        myHtmlData = getData('https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())

        for a in soup.find("div", {'class': 'lBwEZb BL5WZb xP6mwf'}).find_all('a'):
            print(a.get_text())
            speak(a.get_text())

    # The following will ask your choice for news source

    print("\n \nWhich source would you like to hear news from ?")
    print("\n \n1. The Indian Express")
    print("2. BBC News")
    print("3. The Economic Times")
    print("4. Hindustan Times")
    print("5. India Today")
    print("6. NDTV News")
    print("7. CNN-News18")
    print("8. NewsAPI")
    print("9. The Times of India")
    print("10. Tech News from from India Today")
    print("11. Tech news from Gadgets 360 , An NDTV Venture")
    print("12. Sports news from The Indian Express")
    print("13. Google News")

    print("\nYour Choice (Enter the number)")

    userChoice = int(input("Hey User ! Please Enter Your Choice : "))

    if userChoice == 1:
        print("\nNow displaying news from The Indian Express")
        speak("Now displaying news from The Indian Express")
        newsIndianExpress()

    elif userChoice == 2:
        print("\nNow displaying news from BBC News")
        speak("Now displaying news from BBC News")
        newsBBC()

    elif userChoice == 3:
        print("\nNow displaying news from The Economic Times")
        speak("Now displaying news from The Economic Times")
        newsEconomicTimes()

    elif userChoice == 4:
        print("\nNow displaying news from Hindustan Times")
        speak("Now displaying news from Hindustan Times")
        newsHindustanTimes()

    elif userChoice == 5:
        print("\nNow displaying news from India Today")
        speak("Now displaying news from India Today")
        newsIndiaToday()

    elif userChoice == 6:
        print("\nNow displaying news from NDTV News")
        speak("Now displaying news from NDTV News")
        newsNDTV()

    elif userChoice == 7:
        print("\nNow displaying news from CNN-News18")
        speak("Now displaying news from CNN-News18")
        news_news18()

    elif userChoice == 8:
        print("\nNow you will see news from News API")
        speak("Now you will see news from News API")
        newsAPI()

    elif userChoice == 9:
        print("\nNow displaying news from The Times of India")
        speak("Now displaying news from The Times of India")
        newsTOI()

    elif userChoice == 10:
        print("\nNow displaying Technology news from India Today")
        speak("Now displaying Technology news from India Today")
        techNewsIndiaToday()

    elif userChoice == 11:
        print("\nNow displaying Technology news from Gadgets 360, An NDTV Venture")
        speak("Now displaying Technology news from Gadgets 360, An NDTV Venture")
        techNewsGadgets360()

    elif userChoice == 12:
        print("\nNow displaying sports news from The Indian Express")
        speak("Now displaying sports news from The Indian Express")
        sportsIndianExpress()

    else:
        print("\nNow showing news from Google News")
        speak("Now showing news from Google News")
        googleNews()

    # Now Asking User that whether he/she wants to restart the program or not

    restart = input("\nDo you want to see news again (y/n): ")
    if restart == 'y' or restart == 'Y':
        mainProgram()
    else:
        exit()


if __name__ == "__main__":
    mainProgram()
