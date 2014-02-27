#!/usr/bin/env python

# -*- coding: utf-8 -*-


def find_and_retuit():
    """
    For each jail, find tweets inside and retweet
    """
    import codecs
    import requests
    import config
    import os.path
    import dataset
    import lib
    import api
    
    oauth = api.get_oauth()
    
    db = dataset.connect("sqlite:///" + os.path.join(config.local_folder, "tuits.db"))
    
    f = codecs.open(os.path.join(config.local_folder, "carceles_limites.csv"))
    data = f.readlines()
    f.close()
    
    retuits = []
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
                    url = "https://api.twitter.com/1.1/statuses/retweet/"
                    url += str(i['status_id']) + ".json"
                    try:
                        r = requests.post(url=url, auth=oauth)
                        print "Retuited %i" % i['status_id']
                        retuits.append(i['status_id'])
                    except:
                        print "Error", r.text
    
    table = db['tuits']
    for i in retuits:
        data = dict(status_id=i, retuited="yes")
        print data
        table.update(data, ['status_id'])
    

if __name__ == "__main__":
    find_and_retuit()
