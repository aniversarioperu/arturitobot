#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import config
import api
import requests
import lib

if len(sys.argv) < 3:
    print "This script inserts 1 tuit into our database using the status_id value and a string for the jail"
    print "Usage python insert_tuit.py 123208309281908 'Penal Diroes'"
    sys.exit()


oauth = api.get_oauth()

# get tuit data
url = "https://api.twitter.com/1.1/statuses/show.json"
payload = {'id': sys.argv[1].strip()}

r = requests.get(url=url, auth=oauth, params=payload)
data = r.json()

obj = {}
obj['carcel'] = unicode(sys.argv[2].strip(), "utf-8")
obj['created_at'] = data['created_at']
obj['screen_name'] = data['user']['screen_name']
obj['status_id'] = data['id']
obj['text'] = data['text']
obj['user_id'] = data['user']['id']
obj['utc_offset'] = data['user']['utc_offset']
coords = data['geo']['coordinates']
obj['latitude'] = coords[0]
obj['longitude'] = coords[1]

lib.insert_data(obj)
