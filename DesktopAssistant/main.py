import speech_recognition as sr
import win32com.client as wincom
import webbrowser
import openai
import datetime

def say(text):
    speak.Speak(text)

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google_cloud(audio, language="en-in")
            print(f"User said : {query}")
            return query
        except Exception as e:
            return "Some error occurred, try again!"


if __name__ == "__main__":
    speak = wincom.Dispatch("SAPI.SpVoice")
    while True:
        print("Listening...")
        query = TakeCommand()
        say(query)
        sites = [["youtube", "https://www.youtube.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")
