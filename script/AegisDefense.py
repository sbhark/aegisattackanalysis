# Author: shunny 
# Title: AegisDefense Script 
# Description: Script that is called from fail2ban to insert an IP address into a
# database. The script will also be inserting additional information such as date_entered and geolocation of the IP. 

#Imports
import requests
import sys
import logging as logger 

from pymongo import MongoClient
from datetime import datetime
from time import strftime

# Inserts complete ip info to db
def log_info(ip_geo, timestamp, protocol, port, failures): 

    #Create mongo client, database, collection    
    client = MongoClient()
    aegis_database = client['aegis-defense-database']
    ip_collection = aegis_database['ip_blacklist']

    #Construct data for insert
    ip_data = {"ip_geolocation" : ip_geo, "timestamp" : timestamp, "protocol": protocol, "port" : port, "num_failures" : failures}
    insert_id = ip_collection.insert(ip_data)
    logger.info('IP: %s has been inserted into database with id: %s' % (ip_geo['ip'], insert_id))

# Queries freegeoip.net with a http call to get IP geolocation info
def get_ip_geolocation(ip): 
    
    request_url = ('http://freegeoip.net/json/%s' % (ip))
    response = requests.get(request_url)
    ip_geo_info = response.json()

    return ip_geo_info 

# Handles the data that is passed from fail2ban in addition
def handle_data(blocked_ip_info):
    
    #Grab IPGeolocation info 
    ip_geolocation = get_ip_geolocation(blocked_ip_info[0])

    #Convert unix time stamp to datetime
    timestamp = datetime.fromtimestamp(int(blocked_ip_info[4]))

    #Insert all the IP info provided to db
    log_info(ip_geolocation, timestamp, blocked_ip_info[1], blocked_ip_info[2], blocked_ip_info[3]) 

def main():
 
    #logging stuff 
    logger.basicConfig(filename='aegis_defense.log', level=logger.INFO)

    ipinfo = []
    counter = 0

    #Not doing any validation for the values passed in from fail2ban
    #as I'm assuming the avlues are of correct from, ex) ip = ip format.
    for arg in sys.argv:
        if (counter != 0):
            ipinfo.append(arg)                
        
        counter += 1
    handle_data(ipinfo)
    
if __name__ == "__main__": 
    main()
