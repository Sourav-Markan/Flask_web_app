###Flask Web Application Report

##Features:

##Database used is sqlite:
3 Tables:
User 
Brand
Product
Brand and product are linked with the primary key Brand_id

##User can be Two types:
Admin
User
Backend will take care of which email corresponds to admin/user. Multiple emails cant register as Email must be unique.
Passwords are stored in hash form using inbuilt function of FLASK.
Also User Sessions is considered in the web app that means multiple user can access and in front-end it will automatically detect which user is login in that window and it will redirect to that specific User Page. 

#Admin
Can Add New brand {Brand Table}.
Can Add Product corresponding to any Brand {Product Table}.
[NOTE] Both tables are linked using the Brand_id as the Primary Key.
Proper Web interface is available on the Admin screen i.e How many Brands are there in Database and corresponding to them how many Products are Available.
For login as Admin: Email- sourav.markan97@gmail.com  Password - 123456

#User
Web Interface will show the Top Brands (sorted according to number of products they have).
Latest Products will also be shown on screen (that are recently added in database)
Images of product can be easily seen on clicking the link.
Product Detail can to send to his mail id(user) onces, admin config the senders email for the application.
Search Bar is available.
For login as User use: sourav2081997@gmail.com  Password - 123456

Note  New user can also register to the application by filling the details

##Search Bar 
Will consider multiple keywords also example:
Search is tshirt tight (lower/upper doesn’t matter already taken care in the bacgitkend).
Results: Skin tight shirt, high quality Tshirt 
I.e it will consider tshirt and tight as two different key words for query and tries to each keyword match with the substring of name of the product and accordingly gives the result.

##How to use:
Pip3 install < requirement.txt
Python3 run.py 
