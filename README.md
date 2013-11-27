AegisAttackAnalysis
==================

A Python script which is called from fail2ban to store attack IP Addresses into a database for analysis. 

Features 
===================
Stores IP Addresses flagged by fail2ban in a database. 
A basic web application will use the flagged IP database to display information such as number of attacks per IP, 
geo-location of IP, graph of daily total flagged IPs and the most offending IP. 
A daily report can also be sent out for the IPs that have been blacklisted during the day.

Few Things To Note 
===================
Some things to note while I developed this: 

1) I developed this on Mac OSX, tested on a Ubuntu VM and deployed the code to a Debian based server for testing. So all package installation code will work if you use a Debian based OS, such as Ubuntu. 

2) I used Vagrant for local testing! So there are vagrant files in the repo! You don't need them if you don't know how to use vagrant.

3) I haven't tested this yet on a production level system so 1) use this at your own risk 2) if you do use it on a production system and it turns out good feel free to send me an email! :)

4) You can setup a cron so another script will send out daily report emails. The script uses Mandrill to send out the daily email reports. If you don't like Mandrill then feel free to change the code to use your preference for sending out emails. I will be adding support for sending out emails with different APIs and your custom mail servers. 

6) MongoDB! It should be installed on the same machine where the script is running I will add support for using remote mongodb instances. 

7) Thanks for taking a look and using the script :) 

How Tos
===================
To use this script: 

1) Make sure you have Python installed (most Linux OS do)
 - apt-get install python

2) Make sure you have sudo installed 
 - apt-get install sudo

3) Install MongoDB 
 - sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
 - Add to /etc/apt/sources.list: deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen
 - sudo apt-get update 
 - sudo apt-get install mongodb-10gen 
 - More details here: http://docs.mongodb.org/manual/tutorial/install-mongodb-on-debian/

4) Install python-dev and build-essentials
 - sudo apt-get install python-dev build-essentials 

5) Install python-pip
 - sudo apt-get install python-pip

6) Install PyMongo (Python driver for MongoDB)
 - sudo pip install pymongo

7) Install requests 
 - sudo pip install requests

8) Install GIT to pull down the source
 - sudo apt-get install git-core
 - Configure git
 - git clone https://github.com/sbhark/aegisattackanalysis.git

9) Call the script from fail2ban
 - go to /etc/fail2ban/jail.conf
 - go to banaction= and see what it says: ie. iptables-multi
 - open file /etc/fail2ban/action.d/(what it said in the above line).conf
 - insert the following line into where actionban is: python /directory/where/script/is/stored/AegisDefense.py \<ip\> \<protocol\> \<port\> \<failures\> \<time\>
 - example: actionban = iptables -I fail2ban-\<name\> 1 -s <ip> -j DROP
            python /root/script/AegisDefense.py \<ip\> \<protocol\> \<port\> \<failures\> \<time\> 

10) That's it! But if the above is too much for you I created an installation script of all the necessary packages in the installation folder :)

Whenever there is an IP that is blacklisted fail2ban will call this script and the script in turn will write the IP to the database along with some additional informaiton. 

Set up Cron for Daily Report:

1) I assume you are familiar with setting up cron on Linux if not read this: http://v1.corenominal.org/howto-setup-a-crontab-file/

2) You need Mandrill to have a Mandrill API Key if you don't have one they are free to sign up with: http://mandrill.com/

3) Insert the following cronjob: 
 - 00 00 * * * python /path/to/AegisDefenseCron.py 

4) Open AegisDefenseCron.py in a texteditor and edit the following variables. 
  - recipient_email 
  - recipient_name 
  - sender_email
  - from_name 
  - api_key 

5) That's it! A report will be sent out every day at midnight.

Note: For future Release
 
To use the included web-app: 

1) Make sure you have python installed (most Linux OS do) 

2) Make sure you have a web server installed, apache2 / nginx doesn't matter 

3) Install python-pip 
 -  sudo apt-get isntall python-pip -y 

4) Install Django 
 - sudo pip install Django

Road Map
=================
1) Add support for remote database 

2) Web Application for displaying results from db 

3) What else do you want? 

Contact 
==================
If there are any bugs or feature requests you may have then feel free to send me an email. 
EmaiL: ishunny [at] naver.com

