from cgitb import enable
import pyttsx3                                  #Lib for Text to Speech conversion
import datetime as dt                           #Lib for date and time
import speech_recognition as sr
import webbrowser as wb
import pyowm
import wikipedia
import pyaudio
import wolframalpha
import pyjokes

engine = pyttsx3.init('sapi5',True)

voice= engine.getProperty('voices') 

engine.setProperty('voice', voice[1].id)

def speak(audio):                               #Function for converting text into audio

 engine.say(audio)
 engine.runAndWait()

def WishMe():                                    #Function for wishing according to time
    hr=int(dt.datetime.now().hour)
    if hr>=0 and hr<12:
        speak("Good Morning Ajay !")
    elif hr>=12 and hr<15:
        speak("Good Afternoon Ajay!")
    else:
        speak("Good Evening  Ajay !")

    speak("I am eera Your Personal Voice Assistant. How are you Master?")            


def takeCommand():                          #function for taking input from user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)              #without this voice assisant will forever be in listening mode
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
     print("Recoginizing.....")
     query = r.recognize_google(audio, language='en-in') 
     #print(f"User said: {query}\n")
     #speak((f"User said: {query}\n"))

    except Exception as e:
    #print(e)

     speak("Say that again please....") 
     return "None"

    return query    
if __name__=="__main__":
    #speak("Hiii Ajay, I am Kira Your Personal Voice Assistant. How are you? What can I do for you,Today.")
    WishMe()
    while True:

       query = takeCommand().lower()
       if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query=query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

       elif 'power off' in query:
         speak("Let me know if I can help you with anything in Future. powering off....")
         exit()

       elif 'open youtube' in query:
         wb.open("https://www.youtube.com")

       elif 'open google' in query:
          wb.open("https://www.google.com/")

       elif 'open leetcode' in query:
         wb.open("https://leetcode.com/problemset/all/")

       elif 'today temperature' in query: 
         owm=pyowm.OWM('e0be5eff78fe8da457c6c0d8a12f2833')
         mng = owm.weather_manager()
         obs = mng.weather_at_place("Dehradun")
         weather = obs.weather
         print(weather)
         speak(weather)
       elif "hello" in query or "hi" in query:
        speak("Hello Ajay !!! I hope you are doing well")  
       elif "how are you" in query:
            speak("I am fine, Thank you")
            speak("How are you, Ajay")
 
       elif 'fine' in  query or "good" in query:
            speak("It's good to know that you are fine Ajay")
            speak("What can I do for you today?")
    
       elif " gf" in query or " bf" in query or " girlfriend" in query: 
            speak("I'm not sure about, may be you should give me some time")

       elif "i love you" in query:
            speak("It's hard to understand")

       elif 'joke' in query:
            speak(pyjokes.get_joke())
       elif "who i am" in query or "who am i" in query:
            speak("If you talk then definitely your human.")
 
       elif "why you came to world" in query:
            speak("Thanks to Ajay. further It's a secret")

       elif "who are you" in query:
            speak("I am eera Version 1.0 Speed 4.3 teraBytes. A Personal Voice assistant created by Master Ajay")
 
       elif 'reason for your creation' in query:
            speak("I was created as a Minor project by Master Ajay ")
 
 
       
        
