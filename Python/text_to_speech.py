import pyttsx3
from playsound import playsound

engine = pyttsx3.init()
voices = engine.getProperty("voices")
text = "Mic testing 1 2 3"
engine.setProperty("rate", 200)
engine.setProperty("voice", voices[1].id) #voices[1] is for female voice and voice[0] is for male voice

engine.say(text)
engine.runAndWait()
