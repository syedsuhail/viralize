Introduction
===========

Viralize is an application that lets users create and publish their posts across multiple social media platforms (eg. Twitter, Facebook, Blogger) 

Instructions
============
The channels which are being used in the application should authenticate the user.

1.Create .INI file with the list of channels and messages. [example.ini](https://github.com/syedsuhail/viralize/blob/master/viral.ini)

2.Call the setup file along with the .INI file
		
		./viralise example.ini

One Page Spec
=============

 1. User Interface Level --> Get input from user (input as ini file): 

 	 	  get_user_data(filename) -> returns json data(named as data

	     show_info_message(message,type(like error, hint etc)) 
     
 

 2.  Publish Level --> Manages the publishing of the message
       
		publish() --> given a list of dictionaries , for each channel  appropriate publish function is called

		individual social media modules (like twitter_publish module, facebook_publish module etc)
