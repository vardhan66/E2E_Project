import smtplib
from email.message import EmailMessage
import ssl

class SendMail:
    def __init__(self, data):
        self.data = data
        self.sender = 'greviencevvit@gmail.com'
        self.password = 'Saketh@4230'

    def setMail(self, receiver, subject, body):
        mail = EmailMessage()
        mail['From'] = self.sender
        mail['To'] = receiver
        mail['subject'] = subject
        mail.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.sender, self.password)
            smtp.sendmail(self.sender, receiver, mail.as_string())

    def sendMail(self):
        receiver = self.data['email']
        subject = 'Your OTP Code'
        body = self.data['otp']  # Assuming the OTP is passed in the data dictionary
        self.setMail(receiver, subject, body)

if __name__ == "__main__":
    # Assuming 'data' contains the required information
    data = {
        # 'name': 'John Doe',
        # 'year': '2nd',
        # 'who': 'student',
        # 'dept': 'CSE',
        # 'reg_number': '123456',
        'email': '21bq1a4210@vvit.net',
        # 'type_of_grievance': 'Academic',
        # 'complant': 'I have a concern about the course material.'
    }

    # Create an instance of the SendMail class with 'data'
    mail = SendMail(data)
    print("mail send")