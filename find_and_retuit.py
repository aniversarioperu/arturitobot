#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
For each jail, find tweets inside and retweet
"""
import codecs
import config
import os.path
import dataset
import lib

db = dataset.connect("sqlite:///" + os.path.join(config.local_folder, "tuits.db"))

f = codecs.open(os.path.join(config.local_folder, "carceles_limites.csv"))
data = f.readlines()
f.close()

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

        # get tweet ids
        res = db.query("select * from tuits where carcel='" + penal +"' and retuited='no'")
        for i in res:
            if lib.tuit_inside_jail(i['status_id'], poly) == True:
                print unicode(i)

