#!/usr/bin/env python

import dataset
import sqlalchemy
import short_url
import sys
import time
import os
import config
import datetime
import codecs
import lib

dbfile = os.path.join(config.local_folder, "tuits.db")
db = dataset.connect("sqlite:///" + dbfile)
table = db['tuits']

f = codecs.open(os.path.join(config.local_folder, "carceles_limites.csv"))
data = f.readlines()
f.close()

tuits_to_update = []
for i in data:
    i = i.strip()
    if i.startswith("Carcel,"):
        continue
    else:
        i = i.split(",")
        penal = i[0]

        poly = []
        for j in i[1:]:
            j = j.split(" ")
            coord = (float(j[0]), float(j[1]))
            poly.append(coord)

        res = db.query("select * from tuits where carcel='" + penal + "'")
        table = db['tuits']
        for i in res:
            if lib.tuit_inside_jail(i['status_id'], poly) == True:
                dic = {"id": i['id'], "in_jail":"yes"}
                tuits_to_update.append(dic)
            else:
                dic = {"id": i['id'], "in_jail":"no"}
                tuits_to_update.append(dic)




for i in tuits_to_update:
    j = {}
    j['in_jail'] = i['in_jail']
    j['id'] = i['id']
    print j
    table.upsert(j, ['id'])
