#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import dataset
from lib import calc_distance


penal = u"Penal Santa Mónica"
coord = [-12.173532,-77.019076]

def delete(penal, coord):
    db = dataset.connect("sqlite:///tuits.db")
    table = db['tuits']
    res = table.find(carcel=penal)

    to_delete = []
    for i in res:
        dist = calc_distance(coord[0],coord[1],i['latitude'],i['longitude'])
        if dist > 1.1:
            to_delete.append(i['id'])

    for my_id in to_delete:
        print "Removing %i" % my_id
        table.delete(id=my_id)

f = codecs.open("carceles.txt", "r", "utf-8")
penales = f.readlines()
f.close()

for i in penales:
    i = i.strip().split(",")
    penal = i[0]

    j = i[1].split(" ")
    coord = [float(j[0]), float(j[1])]

    delete(penal, coord)
