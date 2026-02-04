import speech_recognition as sr
import webbrowser
import pyttsx3
import time

r=sr.Recognizer()

engine = pyttsx3.init()
# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"
def speak(i):
    engine.say(i)
    engine.runAndWait()
def yes():
    with sr.Microphone() as m:
        print("Listening...")
        data=r.listen(m)
    info=r.recognize_google(data).lower()
    return info
while True:
    command=yes()
    if "hello" in command:
        speak("I am Activated...")
        while True:
            command=yes()
            
            print()
            time.sleep(1)
            print('command')
            if "google" in command:
                command=yes()
                print("you said: ", command)
                webbrowser.open("https://www.google.com/")
                speak("google open ho gya")
            elif "facebook" in command:
                command=yes()

                print("you said: ", command)
                webbrowser.open("https://www.facebook.com/")
                speak("Facebook open ho gya")
            elif "exit" in command:
                command=yes()

                break
    else:
        print("Smjh ni a ya")


        


    





