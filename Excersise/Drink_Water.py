import time
import pyttsx3 as py

def drinkwater():
    while True:
        time.sleep(7200)
        py.speak("Drink Water")

drinkwater()