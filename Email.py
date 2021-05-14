import smtplib, ssl, getpass
from creds import email,epassword
class Email(object):
    def __init__(self,otp,rEmail):
        self.OTP=otp
        self.REmail=rEmail
        self.port = 465  # SSL port
        self.smtp_server = "smtp.gmail.com" # smtp server address
        creds = self.login_credentials()    # Sender credentials
        self.sender_email = creds["email"]  # Senders email
        self.password = creds["pass"]       # Senders password
        # Create a secure SSL context
        self.context = ssl.create_default_context()
    

    def login_credentials(self):
        """ The senders login credentials - password is hidden. """
        sender_email = email
        password = epassword
        return {"email":sender_email, "pass":password}

    def message(self):
        """ Subject and message content """
        subject = "Subject: OTP FOR PROTEKT LOGIN"
        message = "HERE IS YOUR OTP FOR LOGIN : " + self.OTP
        return str(f"Subject: {subject}\n\n" f"{message}")

    def send_mail(self):
        """ Email control and forwarding """
        receiver_email = self.REmail # Receivers email
        message = self.message()
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=self.context) as server:
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, receiver_email, message)
                print("\nEmail successfully sent!")
        except:
            print("\nError occurred while trying to send the email.. Please try again.")


'''if __name__ == "__main__":
    email = Email("ye le kardiya daalde ab otp","hawaskapujari069@gmail.com")
    email.send_mail()'''
"""pjn7190@gmail.com"""
