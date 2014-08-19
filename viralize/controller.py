import json
import cli
import publish

#argument recive from user interface as the json object
filename = cli.filename
data = cli.get_user_data(filename)

def engine_controller():
    channels=publish.list_channels()
    for i in data:
        if data[i]['channel'] in channels:
           publish.publish(data[i]['channel']) 
        else:
            print "Error"
    




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
