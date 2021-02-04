import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for y in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(y)

for x in mycol.find({},{ "address": 0 }):
  print(x)