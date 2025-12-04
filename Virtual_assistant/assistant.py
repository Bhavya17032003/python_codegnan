import datetime
import speech_recognition as sr
import webbrowser
import os
import pyttsx3

# create engine for text to speech
engine = pyttsx3.init()

#speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# take command function
def take_command():
    listener = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listining.....")
        audio = listener.listen(source)
        try:
            command = listener.recognize_google(audio)
            command = command.lower()
            print("Your said: ", command)
            return command
        except:
            print("Sorry, I didn't get that.")
            return ""

# run assistant
def run_assistant():
    command = take_command()
    #if command contains time
    if 'time' in command:
        time = datetime.datetime.now().strftime("%I: %M %p")
        speak("Current time is:" + time)
        print("Current time is:", time)

    # if command contins open notepad
    elif  'open notepad' in command:
        speak("Opening Notepad.....")   
        print("Opening Notepad.....")
        os.system('notepad')

        
    # if command contins open youtube
    elif  'open youtube' in command:
        speak("Opening youtube...")   
        print("Opening youtube...")
        webbrowser.open("https://www.youtube.com/")

           
    # if command contins hey alexa
    elif 'hey alexa' in command:
        query = command.replace("hey alexa", "").strip()
        if query:
            url = f"https://www.google.com/search?q={query}"
            speak(f"Searching for {query}")
            print(f"Searching for {query}")
            webbrowser.open(url)
        else:
            speak("What do you want me to search for ?")
            print("What do you want me to search for ?")
    # if command contains stop 
    elif 'exit' in command:
        speak("Okay, bye bye see u again")
        exit()
    else:
        speak("I am here to assist you ask like current time, \nopen youtube, \nsearch for something......")
        print("I am here to assist you ask like current time, \nopen youtube, \nsearch for something......")

# main
if __name__=="__main__":
    name = input("Enter your name:")
    speak(f"Hey Hii {name}, I am here to assist you ask like current time, \nopen youtube, \nsearch for something......")
    while True:
        run_assistant()


