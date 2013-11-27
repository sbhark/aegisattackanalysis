# Author: shunny
# Title: AegisDefenseCron 
# Description: This script will be placed on a cron job and once called it will
# send a daily report out to a specified email with all the blacklisted IPs 
# inserted into the database within the day. The email is sent out using Mandrill
# so your Mandrill API key will need to be inserted. 

#Imports 
from datetime import datetime
from pymongo import MongoClient

import mandrill
import socket
import logging as logger

#Customize your email stuff here
recipient_email = ''
recipient_name = ''
sender_email = ''
from_name = ''

#Insert your own api key here
api_key = ''

# Gets data from the database to generate info for the daily reports
def get_data_from_db_top_5():
    
    client = MongoClient()
    aegis_database = client['aegis-defense-database']
    ip_collection = aegis_database['ip_blacklist']
    cursor = ip_collection.find().sort([('timestamp', -1)]).limit(5)
    ip_entries = cursor[:]

    top_5_today = []

    for ip in ip_entries: 
        top_5_today.append(ip['ip_geolocation']['ip'])

    return top_5_today

# Send daily report out to a specified email 
def send_daily_report(top5):

    ips = ''
    for ip in top5:
        ips += ('<li> %s </li>' % (ip))

    hostname = socket.gethostname()
    subject = ("%s fail2ban Daily Report" % (hostname))

    email_html = ('<h2>Fail2Ban Email Report from one of your servers </h2> <h3>5 BlackListed Ips today <h3> <p> %s </p>' % (ips))
    try: 
        mandrill_client = mandrill.Mandrill(api_key)
        message = {'from_email': sender_email, 'from_name': from_name, 'global_merge_vars': [{'content': 'merge1 content', 'name': 'merge1'}], 'headers': {'Reply-To': sender_email}, 'html': email_html, 'important': False, 'inline_css': None, 'subject': subject, 'to': [{'email': recipient_email, 'name': recipient_name, 'type': 'to'}], 'track_clicks': None, 'track_opens': None, 'tracking_domain': None, 'url_strip_qs': None, 'view_content_link': None}
        
        response = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
    
    except mandrill.Error, e: 
        logger.info("Error sending out email")
        raise 


# Main method to get and send daily report 
def run_daily_report():

    #Logger stuff 
    logger.basicConfig(filename='aegis_defense_cron.log', level=logger.INFO)
    
    if (recipient_email == '' or api_key == '' ): 
        logger.info('Cannot proceed email or mandrill_api_key field is empty')
    else:
        top_5_offenders = get_data_from_db_top_5()
        send_daily_report(top_5_offenders)         

if __name__ == "__main__": 
    run_daily_report()


