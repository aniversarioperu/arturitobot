#!/usr/bin/env python
# -*- coding: utf-8 -*-
import dataset
import sqlalchemy
import codecs
import short_url
import sys
import time
import datetime
from lib import calc_distance

"""
Update our database with new data fields

* 2013-11-30  short_url
* 2013-11-30  unix timestamp
"""



def update(penal, coord, res):
    data = []
    for i in res:
        if "latitude" in i:
            if i['latitude'] != None:
                if calc_distance(coord[0], coord[1], i['latitude'], i['longitude']) < 1.1:
                    dist = calc_distance(coord[0], coord[1], i['latitude'], i['longitude'])
                    if i['carcel'] == None:
                        print i['id'], dist
                        dic = {}
                        dic["carcel"] = penal
                        dic['id'] = i['id']
                        data.append(dic)
    for i in data:
        j = {}
        j['carcel'] = i['carcel']
        j['id'] = i['id']
        table.upsert(j, ['id'])

db = dataset.connect("sqlite:///tuits.db")
table = db['tuits']

res = db.query("SELECT * from tuits")
penal = "Penal Maranguita"
coord = [-8.409885,-74.55284]
update(penal, coord, res)
