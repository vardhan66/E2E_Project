import smtplib
from email.message import EmailMessage
import ssl
# from .models import StudentModel, CounsellorModel

def SentOTP():
    sender = 'greviencevvit@gmail.com'
    password = 'pvhr wbrs tmbv rxty '

    # std = StudentModel.objects.filter(registration=data['registration']).values()

    # counsellor = std[0]['counsellor']

    # mail = CounsellorModel.objects.filter(id = counsellor).values()[0]['email']
    # print(data['email'])
    receiver = "21bq1a4210@vvit.net"

    subject = 'Your OTP'

    body = 'OTP: 12345'

    mail = EmailMessage()
    mail['From'] = sender
    mail['To'] = receiver
    mail['subject'] = subject
    mail.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, mail.as_string())

if __name__ == '__main__':
    SentOTP()
    print('OTP send')