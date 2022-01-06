import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def post(to_email, message):
    
    msg = MIMEMultipart("alternative")
    
    password = "gr250397"
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
    except:
        server.quit()    
        return True
    else:    
        server.quit()
        return False