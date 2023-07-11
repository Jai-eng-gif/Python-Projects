import os
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
print("Welcome to Robo-Speaker\n")
while True:
    cmd = input("Enter what you want me to speak: ")
    if cmd == 'q':
        speaker.Speak("Bye Bye see u later")
        break
    speaker.Speak(cmd)
