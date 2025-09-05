import time
import pyttsx3

a = int(input("Enter the time in seconds: "))
engine = pyttsx3.init()
engine.setProperty("rate",100)
engine.say("beep")
time.sleep(a)
engine.runAndWait()