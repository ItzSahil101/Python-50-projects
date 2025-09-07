import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os

# print("Running")
def sptext():
    recog = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recog.adjust_for_ambient_noise(source)
        audio = recog.listen(source)
        try:
            print("recognizing..")
            data = recog.recognize_google(audio)
            # speechtx(data)
            print(data)
            return data
        except sr.UnknownValueError as e:
            print("Not Understand!!")
            return ""

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 140)
    engine.say(x)
    engine.runAndWait()

# sptext()
# speechtx("Code Spire")

if __name__ == '__main__':

    if "start" in sptext().lower():
        data1 = sptext().lower()

        if "your name" in data1:
            name = "my name is bro"
            speechtx(name)
        elif "who is sahil jogi" in data1:
            whois = "He is a fullstack website developer and python developer and also a ethical hacker"
            speechtx(whois)
        elif "more about sahil" in data1:
            more = "He loves to play football, chess and learning coding, hacking and understanding networking how thing works"
            speechtx(more)
        elif "what is time" in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif "youtube" in data1:
             webbrowser.open("https://www.youtube.com/")
        elif "my youtube" in data1:
            webbrowser.open("https://www.youtube.com/@CodeSpire2xz")
        elif "joke" in data1:
            joke_1 = pyjokes.get_joke(language="en", category="neutral")
            print(joke_1)
            speechtx(joke_1)
        elif "open file" in data1:
           os.startfile("C:\\")
    else:
        print("say bro code properly")