#!/usr/bin/env python

# -*- coding: utf-8 -*-
import codecs
import sys
import json
import dataset
import sqlalchemy


filename = sys.argv[1].strip()

f = codecs.open(filename, "r", "utf-8")
data = json.loads(f.read())
f.close()

db = dataset.connect("sqlite:///tuits.db")
table = db.create_table("tuits")
table.create_column('utc_offset', sqlalchemy.Integer)
table.create_column('user_id', sqlalchemy.BigInteger)
table.create_column('screen_name', sqlalchemy.Text)
table.create_column('status_id', sqlalchemy.BigInteger)
table.create_column('text', sqlalchemy.Text)
table.create_column('created_at', sqlalchemy.String)
table.create_column('latitude', sqlalchemy.Float)
table.create_column('longitude', sqlalchemy.Float(precision=7))


for obj in data['results']:
    if not table.find_one(status_id=obj['status_id']):
        table.insert(obj)

