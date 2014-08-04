INTRODUCTION
------------

Viralize is an application that lets users create and publish their posts across multiple social media platforms (eg. Twitter, Facebook, Blogger) 

PROPOSED USAGE
--------------

viralize --twitter --facebook --blogger message 

REQUIREMENTS
-------------

1. Takes either file as an input or allows user to enter text
2. User adds title
3. Single authentication for multiple social platforms
4. Publish to social media of choice


ONE PAGE SPEC
-------------

1. Controller part (viral_control)
   	  a. Takes in argument and imports the relevant social media modules
	      
2. Blogger module (viral_blogger)
	  a. Takes the meassage and posts it on blogger
	  b. Returns the url of the blog post

3. URL shortener module	(viral_shortener)
   	   a. Takes the blog url
	   b. Returns shortened url or failure status

4. Twitter module (viral_twitter)
   	   a. Takes the shortened url and title
	   b. Posts the title and shortened url on twitter
	   c. return success or failure status

5. Facebook module (viral_facebook)
   	    a. Takes the shortened url, title and message
	    b. Posts the title along with first few senteces with short url in the end.
	    c. Returns success status or failure status 
	   

