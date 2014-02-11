#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dateutil.relativedelta
import config
import api
import requests
import argparse
import sys
import time
from datetime import datetime
from datetime import timedelta
import os.path




def dict_to_csv(tuit):
    out = ""
    out += str(tuit['id']) + ","
    try:
        out += str(tuit['lat']) + ","
    except:
        out += ","

    try:
        out += str(tuit['long']) + ","
    except:
        out += ","

    clean = datetime.strptime(tuit['datetime'], '%a %b %d %H:%M:%S +0000 %Y')
    offset_hours = -5
    local_time = clean + timedelta(hours=offset_hours)
    final_time = datetime.strftime(local_time, '%Y-%m-%d %I:%M:%S %p')

    out += final_time + "\n"
    return out



def main():
    description = """Get the location of tuits for user"""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-u', '--user', action='store', metavar='twitter user handle',
            required=True, dest='user')

    args = parser.parse_args()


    if args.user:
        oauth = api.get_oauth()

        if os.path.isfile('user_tuits.csv'):
            f = open('user_tuits.csv', 'r')
            lines = f.readlines()
            f.close()

            last_line = lines[-1]
            max_id = last_line.split(",")[0]
            print max_id
        else:
            max_id = ""
            print "no file yet"

        # get tuits
        url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
        params = {'count': 3200,
                    'screen_name': args.user.strip(),
                    'include_rts': 'false',
                    }
        if max_id != "":
            params['max_id'] = max_id

        r = requests.get(url=url, auth=oauth, params=params)
        data = r.json()
        for i in data:
            tuit = {}
            tuit['id'] = i['id']

            if 'geo' in i:
                if i['geo'] != None:
                    tuit['lat'] = i['geo']['coordinates'][0]
                    tuit['long'] = i['geo']['coordinates'][1]

            if 'lat' in tuit:
                tuit['datetime'] = i['created_at']

                csv = dict_to_csv(tuit)
                f = open('user_tuits.csv', 'a')
                f.write(csv)
                f.close()






if __name__ == "__main__":
    main()
