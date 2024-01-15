import speech_recognition as sr
import win32com.client as wincom

def say(text):
    speak.Speak(text)


if __name__ == "__main__":
    speak = wincom.Dispatch("SAPI.SpVoice")
    say("Hello i am Sahil AI")