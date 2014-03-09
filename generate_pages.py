#!/usr/bin/env python

# -*- coding: utf-8 -*-

import dataset
import re
import codecs
import config
import os.path
import subprocess
import shutil


def generate_pages():
    db = dataset.connect("sqlite:///tuits.db")

    res = db.query("select * from tuits")

    out = ""
    for i in res:
        if i['latitude'] != None and i['longitude'] != None:
            out += '["' + str(i['status_id']) + '",'
            out += '"' + i['screen_name'] + '",'
            out += str(i['latitude']) + "," + str(i['longitude']) + "],\n"

    out = re.sub(",$", "", out)

    f = codecs.open("base.html", "r", "utf-8")
    base_html = f.read()
    f.close()

    html = base_html.replace("{% content %}", out)

    index_dest = os.path.join(config.base_url, "index.html")
    f = codecs.open(index_dest, "w", "utf-8")
    f.write(html)
    f.close()
    
    cmd = "rsync -avu avatars " + os.path.join(config.base_url, ".")
    p = subprocess.check_call(cmd, shell=True)

    cmd = "rsync -avu img " + os.path.join(config.base_url, ".")
    p = subprocess.check_call(cmd, shell=True)

    cmd = "rsync -avu bootstrap " + os.path.join(config.base_url, ".")
    p = subprocess.check_call(cmd, shell=True)

    shutil.copy2("jumbotron-narrow.css", os.path.join(config.base_url, "jumbotron-narrow.css"))

def main():
    generate_pages()


if __name__ == "__main__":
    main()
