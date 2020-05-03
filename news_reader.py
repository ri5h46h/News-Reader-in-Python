'''#newspaper reader
def speak(str):
    from win32com.client import Dispatch 
    speak = Dispatch("sapi.SpVoice")

    speak.Speak(str)

if __name__ == '__main__':'''

'''def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)'''
import pyttsx  # pip install pyttsx
engine = pyttsx.init('sapi5')
newVoiceRate=135
engine.setProperty('rate', newVoiceRate)
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
    import requests
    import json
    url = ('http://newsapi.org/v2/top-headlines?country=in&apiKey=a5b172a2897744d9af10f51fa659197e')

    response = requests.get(url)
    text = response.text
    my_json = json.loads(text)
    for i in range(0,11):
        speak(my_json['articles'][i]['title'])
        print(my_json['articles'][i]['title'])


    














        
      


