#!/usr/bin/env python

import dataset
import sqlalchemy
import short_url
import sys
import time
import datetime


"""
Update our database with new data fields

* 2013-11-30  short_url
* 2013-11-30  unix timestamp
"""

db = dataset.connect("sqlite:///tuits.db")
table = db['tuits']


res = db.query("SELECT * from tuits")

data = []
for i in res:
    dic = {"id": i['id'], "retuited":"no"}
    data.append(dic)



for i in data:
    j = {}
    j['retuited'] = i['retuited']
    j['id'] = i['id']
    table.upsert(j, ['id'])
    print i
sys.exit()
