import pyttsx3

text = input("-->")
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()