Viralise
-----------------------

The broadcaster to all kind of social media in a single click.

The software has 3 levels
1.User promt level
2.viralise pool level
3.broadcaster level

User promt level
----------------
----------
	* 	Take input from user.
	*	Message,list of social media which are give to viralise pool
            *	Then give additional arguments if any.

Viralise pool level
-------------------
-------

	*	Check the authentication
	*	Check it wheather the content is acceptable by the social media.
        		*	like twitter can't accept more than 140 characters.
	*	Change to appropriate message content and give to the broadcaster.

Broadcaster
------------
-------

	*	Each social media have a it's own broadcaster.
	*	With the corresponding message content create an requests.
	*	And send these requests to corresponding social media servers.
	*	Display results.
    
Functions and Arguments
-----------------------
----------

Level 1
-------
--
# read_input(message,list_of_channel)
        It read the message content and list of channels from the user.
# validator(message,list_of_channel)
        It check the message content and list of channel wheather it is valid.If it is valid return message and list_of_channel.

Level 2
-------
--
# authenticator(key,list_of_channel)
        *key : Here key is the authentication tool which is used by this application.
        If the authentication is success and have permission to each chanel that in list_of_channel then retun success status.
# distributor(status,message) 
        If the status is success then it return the message as the required format (twitter only support 140 charcters so the message having more than 140 charcter it's convert the message into small part and make an url link) to channel which is in the list_of_channel.Like,
                * facebook_message
                * twitter_message
                * blog_message
                  etc..

Level 3
-------
--
# facebook_broadcaster(facebook_message)
        Send an request to the facebook server to post the message.
# twitter_broadcaster(twitter_message)
        Send an request to the twitter server to tweet the message.
#blog_broadcaster(blog_message)
        Send an request to the blog server to publish the message.







