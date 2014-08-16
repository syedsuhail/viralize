Introduction

	Viralize is an application that lets users create and publish their posts across multiple social media platforms (eg. Twitter, Facebook, Blogger)

It's have 3 level

User interface

	It's only an promt which recives input from user and pass to the controller.The input have the message and list of social medias.And it's also check the validation of message.

Controller

	Controller just pass the message to each viralize channel.

Publish

	For each viralize channel it have an corresponding module.And that module handle channel specific features(Twitter only support 140 character)

	**Authentication
	  --------------
		    Authentication has been done for each channel at the time of setup phase.And it's stored in an hashed format.

 
