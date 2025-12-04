# importing single email sender
from single_email_sender import singleEmailSender
from bulk_email_sender import bulkEmailsender


# main
if __name__ == "__main__":
    print("welcome to email send using python")
    subject = input("Enter subject: ")
    body = input("Enter body msg: ")
    choice = int(input("1. single email \n2. Bulk email \nEnter your operation: "))
    if choice == 1:
        reciever_email = input("Enter receiver email: ")
        # single email function calling
        singleEmailSender(to_email= reciever_email, subject=subject, body=body)
        print(f"{reciever_email} to Email send successfully")
    elif choice == 2:
        # calling bulk email 
        emails = input("Enter list of emails separated by comma: ")
        bulkEmailsender(list_of_emails=emails, subject= subject, body= body)
    else:
        print("select valid operation")
