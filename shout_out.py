import win32com.client

l = ["Mike", "Rohan", "Sam"]

speaker = win32com.client.Dispatch("SAPI.SpVoice")

for i in l:
    speaker.Speak(f"Shout out to {i}")
    if (i == len(l)):
        break
