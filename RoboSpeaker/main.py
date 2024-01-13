import win32com.client as wincom

if __name__ == "__main__":
    print("TEXT TO SPEECH by Sahil Chhoker")
    speak = wincom.Dispatch("SAPI.SpVoice")

    while(True):
        x = input("What you want me to speak : ")
        if(x == 'q'):
            break

        speak.Speak(x)