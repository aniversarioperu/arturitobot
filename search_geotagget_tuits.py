#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dateutil.relativedelta
import datetime
import config
import api
import requests
import argparse
from argparse import RawTextHelpFormatter
import sys
import time
import re
from lib import download_profile_image
from lib import create_database
from lib import insert_data
from lib import calc_distance

def fetch_tuits(geocode, carcel):
    oauth = api.get_oauth()

    url = "https://api.twitter.com/1.1/search/tweets.json" 

    payload = { 'q': '', 
            'geocode':geocode,
            'result_type': 'recent',
            'count': 100 
            }

    #r = requests.get(url=url, auth=oauth, params=payload)
    #data = r.json()
    try:
        next_results = data['search_metadata']['next_results']
        print next_results
    except:
        print "There are not next_results"
        next_results = "None"

    if next_results == "None":
        time.sleep(6)
        next_results = do_request(url, oauth, carcel, payload, geocode)

    while next_results != "None":
        time.sleep(6)
        url = "https://api.twitter.com/1.1/search/tweets.json" + next_results

        payload = None
        next_results = do_request(url, oauth, carcel, payload, geocode)
    

def do_request(url, oauth, carcel, payload, geocode):
    if payload != None:
        r = requests.get(url=url, auth=oauth, params=payload)
        data = r.json()
    else:
        r = requests.get(url=url, auth=oauth)
        data = r.json()
    try:
        next_results = data['search_metadata']['next_results']
        print next_results
    except:
        print "There are not next_results"
        next_results = "None"
    for status in data['statuses']:
        obj = {}
        obj['carcel'] = carcel
        status_id = status['id']
        obj['status_id'] = status_id

        text = status['text']
        obj['text'] = text

        screen_name = status['user']['screen_name']
        obj['screen_name'] = screen_name

        profile_img_url = status['user']['profile_image_url_https']
        download_profile_image(profile_img_url, screen_name)

        utc_offset = status['user']['utc_offset']
        obj['utc_offset'] = utc_offset

        user_id = status['user']['id']
        obj['user_id'] = user_id

        created_at = status['created_at']
        obj['created_at'] = created_at
        
        if 'geo' in status and status['geo'] != None:
            latitude = status['geo']['coordinates'][0]
            longitude = status['geo']['coordinates'][1]
            obj['latitude'] = latitude
            obj['longitude'] = longitude

            if calc_distance(latitude, longitude, float(geocode.split(",")[0]), float(geocode.split(",")[1])) < 1.1:
                print status['text']
                insert_data(obj)

    return next_results

def main():
    description = """Search geotagget tuits"""
    parser = argparse.ArgumentParser(description=description,formatter_class=RawTextHelpFormatter)
    parser.add_argument('-lat', '--latitude', action='store', help='latitude in decimal format',
            required=True, dest='lat')
    parser.add_argument('-long', '--longitude', action='store', help='longitude in decimal format',
            required=True, dest='long')
    parser.add_argument('-rad', '--radius', action='store', help='radius in km',
            required=True, dest='radius')
    parser.add_argument('-c', '--carcel', action='store', 
            help='String used as representadion of carcel:\n\t* diroes',
            required=True, dest='carcel')

    args = parser.parse_args()

    create_database()

    radius = re.search("([0-9]+)", args.radius.strip()).groups()[0] + "km"
    latitude = args.lat.strip()
    longitude = args.long.strip()
    carcel = args.carcel.strip().lower()

    geocode = latitude + "," + longitude + "," + radius

    fetch_tuits(geocode)
    
    
if __name__ == "__main__":
    main()
