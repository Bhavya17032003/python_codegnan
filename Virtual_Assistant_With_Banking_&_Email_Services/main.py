# ---------- IMPORTS ---------- #
import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import os

# ---------- BANK MODULES ---------- #
from bank.login_module import login
from bank.withdraw_module import withdraw
from bank.deposit_module import deposit
from bank.transfer_module import transfer
from bank.ministatement_module import ministatement
from bank.balance_module import balance_enquiry
from bank.logout_module import logout

# ---------- EMAIL MODULES ---------- #
from email_modules.single_email_sender import singleEmailSender
from email_modules.bulk_email_sender import bulkEmailsender

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

# ---------- BANK APPLICATION ---------- #
def bank_application():
    print("\n----- BANK LOGIN -----")
    username = int(input("Enter your account number: "))
    password = int(input("Enter your password: "))

    if login(username, password):
        speak("Login successful!")
        while True:
            print("""
-------------------------------
1. Withdraw
2. Deposit
3. Transfer
4. Mini Statement
5. Balance Enquiry
6. Logout
-------------------------------""")
            choice = int(input("Select operation (1-6): "))

            if choice == 1:
                withdraw(username, int(input("Enter withdraw amount: ")))
            elif choice == 2:
                deposit(username, int(input("Enter deposit amount: ")))
            elif choice == 3:
                receiver = int(input("Enter receiver account number: "))
                amount = int(input("Enter transfer amount: "))
                transfer(username, receiver, amount)
            elif choice == 4:
                ministatement(username)
            elif choice == 5:
                balance_enquiry(username)
            elif choice == 6:
                logout()
                break
            else:
                print("Invalid option.")
    else:
        speak("Login failed!")

# ---------- EMAIL APPLICATION ---------- #
def email_sender():
    speak("Do you want to send a single email or bulk email?")
    choice = take_command()

    subject = input("Enter subject: ")
    body = input("Enter body: ")

    if "single" in choice:
        to_email = input("Enter receiver email: ")
        singleEmailSender(to_email=to_email, subject=subject, body=body)
        speak(f"Email sent to {to_email}")
    elif "bulk" in choice:
        emails_input = input("Enter emails separated by commas: ")
        emails = [email.strip() for email in emails_input.split(",")]
        bulkEmailsender(list_of_emails=emails, subject=subject, body=body)
        speak("Bulk emails sent successfully")
    else:
        speak("Invalid choice. Say 'single' or 'bulk'.")

# ---------- VIRTUAL ASSISTANT ---------- #
def virtual_assistant():
    speak("How can I help you?")
    command = take_command()

    if 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + time)
    elif 'open notepad' in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'search' in command:
        query = command.replace("search", "").strip()
        speak(f"Searching {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif 'send email' in command:
        email_sender()
    elif 'bank' in command:
        bank_application()
    elif 'exit' in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I can tell time, search Google, open YouTube, send emails, or open bank application.")

# ---------- MAIN MENU ---------- #
if __name__ == "__main__":
    speak("Welcome to virtual assistant with banking & email services")

    while True:
        print("""
=====================================
          MAIN MENU
=====================================

1. Bank Application
2. Email Sender
3. Virtual Voice Assistant
4. Exit
""")
        choice = int(input("Select operation (1-6): "))

        if choice == 1:
            bank_application()
        elif choice == 2:
            email_sender()
        elif choice == 3:
            virtual_assistant()
        elif choice == 4:
            speak("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid selection.")
