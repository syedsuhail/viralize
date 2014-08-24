import ConfigParser
import os
import publish_twitter


#checking which is authenticated 
if os.path.isfile('.viralise'):
    cfg = ConfigParser.RawConfigParser()
    cfg.read('.viralise')
    if cfg.has_section('Twitter'):
        Status = cfg.get('Twitter', 'Status')
else:
    Status = publish_twitter.Status 

#Redirect with authenticated status
if Status == None or Status == "Failed":
    publish_twitter.start()
elif Status == "Success":
    publish_twitter.tweet()
