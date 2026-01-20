import time
from plyer import notification
import threading 
import pyttsx3
def speech_remindation():
    engine = pyttsx3.init()
    engine.say("It's been 20 minutes. please take some rest!")
    engine.runAndWait()
def eye_break():
    i=0
    while True:
        notification.notify(title="Eye care",message="Please look away 20 meters its been 20 mins ")
        speech_remindation()
        print(f"round : {i}")
        i=i+1
        time.sleep(20*60)
def eye_blink():
    while True:
        notification.notify(title="Eye blink",message="Blink the eye")
        time.sleep(60)


eye_break_thread=threading.Thread(target=eye_break)
eye_blink_thread=threading.Thread(target=eye_blink)

eye_break_thread.start()
eye_blink_thread.start()


