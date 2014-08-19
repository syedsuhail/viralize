import json
import cli


#argument recive from user interface as the json object
filename = cli.filename
data = cli.get_user_data(filename)


'''Checks the which publish module and pass the pointer to that module'''
def engine_controller():
    i = 0
    lenght = len(data)
    while(i < lenght):
        data_controler = data[i]['channel']
        if data_controler == 'twitter':
            publish_twitter(i)
            i = i + 1
        elif data_controler == 'facebook':
            publish_facebook(i)
            i = i + 1
        elif data_controler == 'blog':
            publish_blog(i)
            i = i + 1
        elif data+_controler == 'mail':
            publish_mail(i)
            i = i + 1
        else:
            print "ERROR Channel not found"

'''The fucation calling are commented over here,because the corresponding function calling has been replace after complete all module in the publish level''' 


#send message to the twitter module
def publish_twitter(i):
    message = data[i]['message']
    #twitter(message)
    return

#send message to the facebook module
def publish_facebook(i):
    message = data[i]['message']
    #facebook(message)
    return


#send message and tittle to the blog module
def publish_blog(i):
    message = data[i]['message']
    tittle = data[i]['tittle']
    #blog(message,tittle)
    return

#send message and subject to the mail module
def publish_mail(i):
    message = data[i]['message']
    subject = data[i]['subject']
    #mail(message,subject)
    return
