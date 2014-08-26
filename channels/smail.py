import smtplib  
import cli
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from binascii import unhexlify  
def compose_mail(fro,to,subject,message):
    msg=MIMEMultipart()
    msg['From']=fro
    msg['To']=to
    msg['Subject']=subject
    body=message
    msg.attach(MIMEText(body,'plain'))
    return msg.as_string()


def gmail(text):
    fro=text['from']
    message=text['message']
    try:
        to=text['to'].split(',')
    except Exception:
        to=text['to']
    subject=text['subject']
    try:
        username,password=cli.get_username_pass('gmail')
    except Exception:
        show_info('no username password')
        return None
    username=unhexlify(username)
    password = unhexlify(password)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    try:
        server.login(username,password)
    except Exception:
        cli.show_info("could not authenticate")
        return None
    try:
        for i in to:
            msg=compose_mail(fro,i,subject,message)
            server.sendmail(fro,i,msg)
            info= "Sent mail to %s"% i
            cli.show_info(info)
    except Exception:
        show_info('could not send')
    
           
       
    server.quit()
    return 1
    
