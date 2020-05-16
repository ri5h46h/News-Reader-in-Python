#News Notification System in Python 
#This code is contributed by Rishabh Narayan 
#Create your API Key from NewsAPI https://www.newsapi.org/ 

from plyer import notification
import requests
import json
from win32com.client import Dispatch

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = 'C:\\Users\\uday_\\Downloads\\Iconsmind-Outline-Newspaper-2.ico',
        timeout = 13,
    )

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':

    response = requests.get('http://newsapi.org/v2/top-headlines?'
                            'country=in&'
                            'apiKey=a5b172a2897744d9af10f51fa659197e')
    text = response.text
    news_json = json.loads(text)
    for i in range(2):
        news = news_json['articles'][i]['title']
        notifyMe("News from Python 3.8.3",news)
        speak(news)
        # print(news)
		
#http://www.iconarchive.com/show/outline-icons-by-iconsmind/Newspaper-2-icon.html
#download the icon from here, download ico file not png...
