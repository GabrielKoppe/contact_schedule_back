import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()
#import data_secret

def post(to_email, ):
    
    msg = MIMEMultipart("alternative")
    
    password = os.environ.get("EMAIL_PASSWORD")
    msg["Subject"] = "Presença confirmada!"
    msg["From"] = "casamento.gab.quel@gmail.com"

    msg.attach(message)

    fp = open('images/image-1.jpeg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

    fp = open('images/image-2.jpeg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<image2>')
    msg.attach(msgImage)

    fp = open('images/image-3.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<image3>')
    msg.attach(msgImage)

    # Create secure connection with server and send email
    try:
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

        # Login Credentials for sending the mail
        server.login(msg['From'], password)

        # send the message via the server.
        server.sendmail(msg['From'], to_email, msg.as_string())
        
        server.quit()
        return True
    except:
        server.quit()    
        return False