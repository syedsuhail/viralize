import os
import ConfigParser
import controller
import smtplib  
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText 


mail_credential = os.path.expanduser('.credentials')



def get_value():
    '''Returns the mail address,password which either taken from the credential file or as in the form of a user direct input. '''
    mail_credential = os.path.expanduser('.credentials')
    cfg = ConfigParser.RawConfigParser()
    cfg.read(mail_credential)
    #mail address taken from the credential file
    if cfg.has_section('mail'):
        try:
            mail_id = cfg.get('mail', 'mailaddres')
            password = cfg.get('mail', 'password')
            return mail_id,password
        except ConfigParser.NoOptionError:
            raise Error
    #Values taken as user input
    else:
        mail_id = controller.get_data('mail address')
        password = controller.get_password('mail password')
        mail_id = mail_id.encode('base64','strict');
        password = password.encode('base64','strict');
        return mail_id,password


def initialise():
    '''Recives values from the get_value function and set in the credential file also returns the mail address,password for sending'''
    cfg = ConfigParser.RawConfigParser()
    #Creates if there no exist an credential file
    if not os.path.exists(mail_credential):
        cfg.read(mail_credential)
        cfg.add_section('mail')
        mail_id,password = get_value()
        cfg.set('mail', 'mailaddres', mail_id)
        cfg.set('mail', 'password', password)
        with open('.credentials', 'wb') as configfile:
            cfg.write(configfile)
            #Read from the credential file
    else:
        cfg.read(mail_credential)
        #Put Values in to the credential file
        if not cfg.has_section('mail'):
            cfg.add_section('mail')
            mail_id,password = get_value()
            cfg.set('mail', 'mailaddres', mail_id)
            cfg.set('mail', 'password', password)
            with open('.credentials', 'wb') as configfile:
                cfg.write(configfile)
        else:
            #Takes values from the credential file
            mail_id,password = get_value()
    

    mail_id = mail_id.decode('base64','strict');
    password = password.decode('base64','strict');
    return mail_id,password


def compose_mail(fro,to,subject,message):
    '''Recives from address,to address,subject and message and returns a composed mail'''
    msg=MIMEMultipart()
    msg['From']=fro
    msg['To']=to
    msg['Subject']=subject
    body=message
    msg.attach(MIMEText(body,'plain'))
    return msg.as_string()




def publish(data):
    '''The mail sending operation on the website has been done and return the status message'''
    mail_id,password = initialise()
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
        return 'The input in mail (to address) may be wrong. Check your input methode'
        
    #checks message is exist
    if 'message' in data:
        if data['message'] != '':
            message = data['message']
        else:
            msg = "Do you want to continue as message in mail as empty(yes/no):"
            request = "Email message"
            y,value = controller.warning(msg,request)
            if  y != 'abcd':
                message = value
            else:
                return 'Given option is wrong:'
    else: 
        return 'The input in mail (message) may be wrong. Check your input methode'
        
    #Checks subject is exist
    if 'subject' in data:
        if data['subject'] != '':
             subject = data['subject']
        else: 
            msg = "Do you want to continue as subject in mail as empty(yes/no):"
            request = "Email Subject"
            y,value = controller.warning(msg,request)
            if  y != 'abcd':
                subject = value
            else:
                return 'Given option is wrong:'

    else:
        return 'The input in mail (subject)may be wrong. Check your input methode'

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
    except Exception:
        return "Check your internet connection"
    server.ehlo()
    server.starttls()
    try:
        server.login(mail_id,password)
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
    
