import datetime, re
from pymongo import MongoClient
client = MongoClient(host='localhost', port=27017)
db = client['insurances_dev']

# Find specific field in many records
# for res in db.info.find({'created_by': re.compile("")}):
#     print(res['created_by'])
# Find field in one record
# mongo.db.info.find_one()['db_created_date']


# print(client.list_database_names())
# print(datetime.datetime.now())
# db = client['insurances_dev']
# print(db)
# # """增加"""
# # # 增加单条
# created_date = {"created_by": 'York'}
# res = db.info.insert_one(created_date)
# print(res.inserted_id)  # 5d2ed8f865d6b8f1c494ff78 ObjectId对象，不是字符串
# db.info.findOne({"created_by":{$exists:true}})["created_by"]

# class DBConfig:
#     def __init__(self):
#         self.client = MongoClient(host='localhost', port=27017)
#         print(self.client.list_database_names())
#         self._create()
#
#     def connect(self):
#         return self.client
#
#     def __del__(self):
#         self.client.close()
#
#
# if __name__ == '__main__':
#     db = DBConfig()
#     db.client.insurances_dev.info.find()
