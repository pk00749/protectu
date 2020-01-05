import datetime
from pymongo import MongoClient

# Create database
client = MongoClient(host='localhost', port=27017)
db = client['protectu']
if 'protectu' not in client.database_names():
    print('protectu not in database, now creating...')
    db.info.insert({"db_created_date": datetime.datetime.now(), 'created_by': 'York'})
else:
    print('protectu exists.')
    print(db.info.find_one())

