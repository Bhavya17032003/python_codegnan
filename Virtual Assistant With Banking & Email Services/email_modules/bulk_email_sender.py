from email_modules.single_email_sender import singleEmailSender

def bulkEmailsender(list_of_emails, subject, body):
    for email in list_of_emails:
        try:
            singleEmailSender(to_email=email, subject=subject, body=body)
        except Exception as e:
            print(f"Failed to send email to {email}. Error: {e}")
