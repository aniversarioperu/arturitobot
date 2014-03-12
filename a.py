import dataset
def delete_old_tuits():
    db = dataset.connect("sqlite:///tuits.db")
    table = db['tuits']
    res = db.query("select * from tuits where in_jail != 'yes'")
    j = 0
    for i in res:
        j += 1
    print j

    res = db.query("select * from tuits where in_jail != 'yes' order by status_id desc")
    j = 0

    to_delete = []
    for i in res:
        j += 1
        if j > 200:
            to_delete.append(i['id'])

    for i in to_delete:
        table.delete(id=i)
        print "deleting ", i

delete_old_tuits()

