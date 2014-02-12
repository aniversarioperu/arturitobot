
def calc_distance(lat1, lon1, lat2, lon2):
    # calcular distancia en km entre dos puntos geograficos usando la formula de
    # Haversine. Fuente: http://gis.stackexchange.com/questions/61924/python-gdal-degrees-to-meters-without-reprojecting
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    from math import cos, sin, asin, sqrt, radians

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km


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

    return screen_name.lower()

def delete_tuits_no_coords():
    import dataset
    # drop tuits with no coordinates
    db = dataset.connect("sqlite:///tuits.db")
    table = db['tuits']
    table.delete(latitude=None)



