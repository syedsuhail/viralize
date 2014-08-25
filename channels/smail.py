import smtplib  
import getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

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
    to=text['to'].split(',')
    print to
    subject=text['subject']
    username= 'ssuhail.ahmed93@gmail.com'
    password = getpass.getpass('Password for gmail $:')
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    for i in to:
        msg=compose_mail(fro,i,subject,message)
        server.sendmail(fro,i,msg)
        print "Sent mail to %s"% i
    server.quit()



