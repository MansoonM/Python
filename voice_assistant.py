"""
Author - bhakti suryawanshi
Docstring - this file gives program for developing personal google assistant
date - 20 dec 2022
"""
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os


try:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def greet():
        hour = int(datetime.datetime.now().hour)
        print(hour)
        if hour>= 0 and hour<12:
            speak("Good Morning !")
        elif hour>= 12 and hour<18:
            speak("Good Afternoon !") 
        else:
            speak("Good Evening !") 
        speak("Welcome , I am your personal voice assistant")

    def VoiceCommand(): 
        r = sr.Recognizer() 
        with sr.Microphone() as source:
            
            print("Recognizing...")
            r.pause_threshold = 1
            audio = r.listen(source) 
        try:
            print("Recognizing...")   
            query= r.recognize_google(audio, language ='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)   
            print("Unable to Recognize your voice.") 
            return "None" 
        return query


    if __name__ == '__main__':
        greet()
        while True: 
            work = VoiceCommand().lower()
            if 'hello' in work:
                speak('hi , how can i help you')
            
            if "wikipedia" in work:
                speak("Searching wikipedia...")
                work = work.replace("wikipedia", "")
                results = wikipedia.summary(work,sentences =5)
                speak("According to wikipedia")
                print(results)
                speak(results)
                
            elif 'open notepad' in work:
                speak('opening notepad for you.......')
                path = ("c:\\windows\\system32\\notepad.exe")
                os.startfile(path)
            elif 'close notepad' in work:
                speak('closing notepad wait.....')
                os.system('c:\\windows\\system32\\taskkill.exe /F /IM notepad.exe')

            elif 'open youtube' in work:
                speak("Here you go to Youtube\n")
                webbrowser.open("https://www.youtube.com/")
    
            elif 'open google' in work:
                speak("Here you go to Google\n")
                webbrowser.open("https://www.google.co.in/")
            
            elif 'play music' in work :
                speak('opening music player....')
                path = ("C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe")
                os.startfile(path)
                
            elif 'open mail' in work:
                speak("Here you go to mail\n")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            
            elif 'open whatsaap' in work:
                speak("opening whatsaap for you\n")
                webbrowser.open("https://web.whatsapp.com/")
            
            elif 'exit' in work:
                speak("Thanks for giving me your time ..... have a nice day....")
                exit()

except BaseException as ex:
    print(f"error occured = {ex}")

finally:
    print("Thank you .....bye..have a nice day")
    