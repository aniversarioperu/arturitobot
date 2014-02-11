#!/usr/bin/env python

# -*- coding: utf-8 -*-

import dataset
import re
import codecs


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

    f = codecs.open("index.html", "w", "utf-8")
    f.write(html)
    f.close()


def main():
    generate_pages()


if __name__ == "__main__":
    main()
