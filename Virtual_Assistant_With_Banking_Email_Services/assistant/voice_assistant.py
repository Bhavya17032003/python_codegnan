import datetime
import pyttsx3
import webbrowser
import os
import speech_recognition as sr
from email_modules.single_email_sender import singleEmailSender
from email_modules.bulk_email_sender import bulkEmailsender

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = listener.listen(source)
    try:
        command = listener.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except:
        speak("Sorry, I didn't catch that.")
        return ""

def email_sender():
    speak("Single or Bulk email?")
    choice = take_command()
    subject = input("Enter subject: ")
    body = input("Enter body: ")

    if "single" in choice:
        to_email = input("Enter receiver email: ")
        singleEmailSender(to_email=to_email, subject=subject, body=body)
    elif "bulk" in choice:
        emails_input = input("Enter emails separated by commas: ")
        emails = [email.strip() for email in emails_input.split(",")]
        bulkEmailsender(emails, subject, body)
    else:
        speak("Invalid choice")

def virtual_assistant():
    speak("How can I help you?")
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + time)
    elif 'open notepad' in command:
        os.system("notepad")
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
    elif 'search' in command:
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif 'send email' in command:
        email_sender()
    elif 'exit' in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I can tell time, search Google, open YouTube, or send emails.")
