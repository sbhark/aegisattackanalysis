AegisAttackAnalysis
===================

A PHP script which is called from fail2ban to store attack IP Addresses into a database for analysis. 

Features 
===================
Stores IP Addresses flagged by fail2ban and stores the IP information in a database. 
A basic web application will use the flagged IP database to display information such as number of attacks per IP, 
geo-location of IP, graph of daily total flagged IPs and the most offending IP. 
