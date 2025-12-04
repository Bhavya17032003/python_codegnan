import datetime
import speech_recognition as sr
import webbrowser
import os
import pyttsx3
from single_email_sender import singleEmailSender
from bulk_email_sender import bulkEmailsender

# ---------- SETUP ---------- #
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen to the user's voice and convert it to text."""
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = listener.listen(source)
    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
        return command
    except:
        speak("Sorry, I didn't catch that.")
        return ""

# ---------- MAIN ASSISTANT ---------- #
def run_assistant():
    command = take_command()

    # 1️. Tell time
    if 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + time)
        print("Current time is:", time)

    # 2️.  Open Notepad
    elif 'open notepad' in command:
        speak("Opening Notepad...")
        os.system('notepad')

    # 3️. Open YouTube
    elif 'open youtube' in command:
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com/")

    # 4️ . Google search
    elif 'hey alexa' in command:
        query = command.replace("hey alexa", "").strip()
        if query:
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            speak("What do you want me to search for?")
            query = take_command()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")

    # 5️. Send email (voice-based)
    elif 'send email' in command:
        speak("Do you want to send a single email or bulk email?")
        choice = take_command()

        if 'single' in choice:
            speak("Please say the receiver email address.")
            to_email = input("Receiver email (type for accuracy): ")

            speak("Please say the subject.")
            subject = take_command()
            if subject == "":
                subject = input("Subject (type if not heard): ")

            speak("Please say the message body.")
            body = take_command()
            if body == "":
                body = input("Body (type if not heard): ")

            singleEmailSender(to_email=to_email, subject=subject, body=body)
            speak(f"Email sent successfully to {to_email}")

        elif 'bulk' in choice:
            speak("Please say all emails separated by commas.")
            list_of_emails = input("Emails (type comma-separated): ")

            speak("Please say the subject.")
            subject = take_command()
            if subject == "":
                subject = input("Subject: ")

            speak("Please say the message body.")
            body = take_command()
            if body == "":
                body = input("Body: ")

            bulkEmailsender(list_of_emails=list_of_emails, subject=subject, body=body)
            speak("Bulk emails sent successfully.")

        else:
            speak("Please say either single or bulk email.")

    # 6️. Exit
    elif 'exit' in command or 'stop' in command or 'quit' in command:
        speak("Okay, bye bye! See you again soon.")
        exit()

    # 7. Default response
    else:
        speak("I can tell the time, open YouTube, search Google, or send emails.")

# ---------- MAIN ---------- #
if __name__ == "__main__":
    name = input("Enter your name: ")
    speak(f"Hey {name}, I am your smart voice assistant! You can ask me to tell time, open YouTube, search Google, or send emails.")
    while True:
        run_assistant()
