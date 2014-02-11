def insert_data(obj):
    import dataset
    db = dataset.connect('sqlite:///tuits.db')
    table = db['tuits']

    if not table.find_one(status_id=obj['status_id']):
        table.insert(obj)    

def create_database():
    import dataset
    import os.path
    database_file = "tuits.db"
    if not os.path.isfile(database_file):
        try:
            print "Creating database"
            db = dataset.connect('sqlite:///' + database_file)
            table = db.create_table("tuits")
            table.create_column('carcel', sqlalchemy.String)
            table.create_column('utc_offset', sqlalchemy.Integer)
            table.create_column('user_id', sqlalchemy.BigInteger)
            table.create_column('screen_name', sqlalchemy.Text)
            table.create_column('status_id', sqlalchemy.BigInteger)
            table.create_column('text', sqlalchemy.Text)
            table.create_column('created_at', sqlalchemy.String)
            table.create_column('latitude', sqlalchemy.Float)
            table.create_column('longitude', sqlalchemy.Float(precision=7))
        except:
            pass

def get_profile_image(url):
    import cStringIO
    import base64
    import requests    
    request_image = requests.get(url)
    i = cStringIO.StringIO(request_image.content)
    return base64.b64encode(i.read())

def download_profile_image(url, screen_name):
    import requests    
    import os.path

    # folder to keep our twitter profile images
    directory = "avatars"

    if not os.path.exists(directory):
        os.makedirs(directory)

    path = screen_name + ".jpg"
    path = os.path.join(directory, path.lower())
    if not os.path.isfile(path):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r.iter_content():
                    f.write(chunk)
    else:
        print "We got avatar for %s" % screen_name

    return screen_name.lower()

