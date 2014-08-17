Introduction
------------

Viralize is an application that lets users create and publish their posts across multiple social media platforms (eg. Twitter, Facebook, Blogger) 



One Page Spec
-------------

1. User Interface Level --> Get input from user (input as ini file)

     -get_user_data(filename) -> returns json data(named as data

     -show_info_message(message,type(like error, hint etc)) 
     
     
2. Controller Level --> Parse json data and pass to appropriate publish channel
   -route(data)
	   
3.  Publish Level --> Manages the publishing of the message
       
	   -publish class (message,social_list) 

	   -individual social media modules (like twitter_publish module, facebook_publish module etc)
	


[Extension part]

Authentication Level --> Manage authentication
	       
	       -Authenticate() -> returns authentication status	       
	    
	       -validate_message()

