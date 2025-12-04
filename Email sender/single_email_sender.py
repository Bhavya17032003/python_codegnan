import smtplib  # simple email transfer protocal
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# sender email details
SENDER_EMAIL = "bhavyasreekanchukommala@gmail.com"
SENDER_PASSKEY = "cqlu knob brti jdxb"
# smtp configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# single email sender function definition 
def singleEmailSender(to_email, subject, body):
    msg = MIMEMultipart()
    msg['To'] = to_email
    msg['From'] = SENDER_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))


    # create server connection
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        # server starts sequerly
        server.starttls()
        # login to server
        server.login(SENDER_EMAIL, SENDER_PASSKEY)
        # send email to to_email
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string()) 
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print("Field to send email to {to_email}:, Error: {e}")
    finally:
         # server quit
        server.quit()
