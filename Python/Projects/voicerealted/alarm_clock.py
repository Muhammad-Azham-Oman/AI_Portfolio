import datetime
import pyttsx3
import time

d = int(input("Enter the hour:"))
b = int(input("Enter the minutes:"))
c = int(input("Enter the seconds:"))

a = f"0{d}:{b}:{c}"

print(a)

while True:
 x = datetime.datetime.now()
 w = x.strftime("%H:%M:%S")
 print(w)

 if w==a:
   engine = pyttsx3.init()
   voices = engine.getProperty("voices")
   engine.setProperty("voice", voices[1].id)
   engine.say("beep")
   engine.runAndWait()
   
   t = 0
   while t < 60:
    engine = pyttsx3.init()
    engine.say("BEEP! BEEP! BEEP!")
    time.sleep(0.1)
    engine.runAndWait()
    t += 1