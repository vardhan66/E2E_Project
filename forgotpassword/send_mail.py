import smtplib
from email.message import EmailMessage
import ssl

class SentOTP:
    def __init__(self, mail_data):
        self.sender = 'greviencevvit@gmail.com'
        self.password = 'pvhr wbrs tmbv rxty'
        self.receiver = mail_data['email']
        self.subject = 'Your OTP'
        self.body = f"OTP: {mail_data['otp']}"

    def sendMail(self):
        mail = EmailMessage()
        mail['From'] = self.sender
        mail['To'] = self.receiver
        mail['subject'] = self.subject
        mail.set_content(self.body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.sender, self.password)
            smtp.send_message(mail)

if __name__=="__main__":
    data= {
        'email' : '21bq1a4210@vvit.net',
        'otp' : 12345,
    }
    SentOTP(data).sendMail()
    print('mail Send')
