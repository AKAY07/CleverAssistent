#importing libraries
from gtts import gTTS
import speech_recognition as sr
import os 
import datetime
import warnings
import calendar
import random
import wikipedia
import webbrowser

warnings.filterwarnings('ignore')

def recordaudio():
   r=sr.Recognizer()

   with sr.Microphone() as source:
       print('say something') 
       audio=r.listen(source) 

       #i am using google speech recognition
       try:
           data=r.recognize_google(audio)
           print('searching:\t'+data)
       except sr.UnknownValueError:
            print('google cannot recognise value') 
       except sr.RequestError as e:
            print('not connected to internet'+e) 

       return data            

def responce(text):
    print(text)
     
    #cnoverting text to speech
    myobj=gTTS(text=text,lang='en',slow=False)

    myobj.save('rep.mp3')

    os.system('start rep.mp3')

    

if __name__== "__main__":

    
    data=recordaudio().lower()

    if 'wikipedia' in data:
        data=data.replace("wikipedia"," ")
        results=wikipedia.summary(data,sentences=3)
        responce(results)
    elif 'open youtube' in data:
        webbrowser.open("youtube.com")
    elif 'open google' in data:
        webbrowser.open("google.com")
