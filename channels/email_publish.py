import os
import ConfigParser
from tests import mock_viralize
import smtplib  
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from binascii import unhexlify  


mail_credential = os.path.expanduser('.credentials')

'''Returns the mail address'''
def get_value():
    mail_credential = os.path.expanduser('.credentials')
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail_credential)
    #mail address taken from the credential file
    if cfg.has_section('mail'):
        try:
            mail_id = cfg.get('mail', 'mailaddres')
            password = cfg.get('mail', 'password')
            username = cfg.get('mail', 'username')
            return mail_id,username,password
        except ConfigParser.NoOptionError:
            raise Error
    #Values taken as user input
    else:
        mail_id = viralize.get_data('mail address')
        username = viralize.get_data('mail username')
        password = viralize.get_password('mail password')
        mail_id = mail_id.encode('base64','strict');
        username = username.encode('base64','strict');
        password = password.encode('base64','strict');
        return mail_id,username,password


def initialise():
    cfg = ConfigParser.RawConfigParser()
    #Creates if there no exist an credential file
    if not os.path.exists(mail_credential):
        cfg.read(mail_credential)
        cfg.add_section('mail')
        mail_id,username, password = get_value()
        cfg.set('mail', 'mailaddres', username)
        cfg.set('mail', 'username', username)
        cfg.set('mail', 'password', password)
        with open('.credentials', 'wb') as configfile:
            cfg.write(configfile)
            #Read from the credential file
    else:
        cfg.read(mail_credential)
        #Put Values in to the credential file
        if not cfg.has_section('mail'):
            cfg.add_section('mail')
            mail_id,username, password = get_value()
            cfg.set('mail', 'mailaddres', mail_id)
            cfg.set('mail', 'username', username)
            cfg.set('mail', 'password', password)
            with open('.credentials', 'wb') as configfile:
                cfg.write(configfile)
        else:
            #Takes values from the credential file
            mail_id,username, password = get_value()
    

    mail_id = mail_id.decode('base64','strict');
    username = username.decode('base64','strict');
    password = password.decode('base64','strict');
    return mail_id,username,password


def compose_mail(fro,to,subject,message):
    msg=MIMEMultipart()
    msg['From']=fro
    msg['To']=to
    msg['Subject']=subject
    body=message
    msg.attach(MIMEText(body,'plain'))
    return msg.as_string()




def publish(data):
    mail_id,username,password = initialise()
    #checks the to address exsist
    if 'to' in data:
        if data['to'] != '':
            try:
                to = data['to'].split(',')
            except Exception:
                to = data['to']
        else:
            return 'The to address could not create as empty'
    else:
        return 'The to address Should be in proper format'
        
    #checks message is exist
    if 'message' in data:
        if data['message'] != '':
            message = data['message']
        else:
            return 'The message could not create as empty'
    else:
        return 'The message Should be in proper format'
        
    #Checks subject is exist
    if 'subject' in data:
        if data['subject'] != '':
             subject = data['subject']
        else:
            return 'The subject could not create as empty'
    else:
        return 'The subject Should be in proper format'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    try:
        server.login(username,password)
    except Exception:
        return "could not authenticate"
    try:
        for i in to:
            msg = compose_mail(mail_id,i,subject,message)
            server.sendmail(mail_id,i,msg)
            info = "Sent mail to %s"% i
            return info
    except Exception:
        return 'could not send'
    
    server.quit()
    
