import smtplib  
import getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from viralize import cli
def compose_mail(fro,to,subject,message):
    msg=MIMEMultipart()
    msg['From']=fro
    msg['To']=to
    msg['Subject']=subject
    body=message
    msg.attach(MIMEText(body,'plain'))
    return msg.as_string()
    

def gmail():
    text=cli.get_user_data('tests/viral.ini')
    fro=text[3]['from']
    message=text[3]['message']
    to=[text[3]['to']]
    subject=text[3]['subject']
    username= 'ssuhail.ahmed93@gmail.com'
    password = getpass.getpass()
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    for i in to:
        msg=compose_mail(fro,i,subject,message)
        server.sendmail(fro,i,msg)
        print "Sent mail to %s"% i
    server.quit()



