def tuit_inside_jail(status_id, poly):
    """
    Finds out whether a tuit has been posted from within a jail based on 
    coordinates of a polygon.
    Using the Ray casting algoritm

    http://stackoverflow.com/a/16625697
    """
    import dataset
    import config
    import os.path
    import math

    db_file = os.path.join(config.local_folder, "tuits.db")
    db = dataset.connect("sqlite:///" + db_file)
    table = db['tuits']
    res = table.find_one(status_id=status_id)
    y = res['latitude']
    x = res['longitude']

    n = len(poly)
    inside = False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside

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
            table.create_column('in_jail', sqlalchemy.String)
            table.create_column('latitude', sqlalchemy.Float)
            table.create_column('longitude', sqlalchemy.Float(precision=7))
            table.create_column('retuited', sqlalchemy.Text)
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

