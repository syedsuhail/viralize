Introduction
------------

Viralize is an application that lets users create and publish their posts across multiple social media platforms (eg. Twitter, Facebook, Blogger) 


Sample Flow
-------------

1. User runs application with message and social platform arguments
2. Application prompts for username and password
3. Controller receives info from from user level.
4. Controller passes username and password(hashed) to authenticator to authenticate the user
   	      *if username password not present then prompts user for a sign up process
5. Controller checks the socail platform list and
   	      *if blogger is one of social platforms:
	      	  -Prompts user for title
		  -Title is validated to be less than 100 characters
		  -Publishes the blog with title and message and returns the url
		  -Controller shortens the url and passes the title and short url to other social platform publishers which publish the title and url
		
	      * If no blogger then :
	      	   -Message is validated to be less than 140 characters
		   -Controller routes message to differnt social publisher
		   -Publishers publish the message on appropriate platforms




ONE PAGE SPEC
-------------

1. User Interface Level --> Get input from user

     *get_message_from_user() -> returns message, social_list
     
     
2. Controller Level --> Perform routing actions on message

	   *shorten_url(url) -> returns shortened url

	   *route_message(message,social_list) -> returns status for routing to each social_module

	   
3.  Publish Level --> Manages the publishing of the message
 	       
	       *publish_module (message,social_list) --> returns status(successor failur)




[Extension part]

Authentication Level --> Manage authentication
	       
	       *Authenticate() -> returns authentication status	       
	       *validate_message()

