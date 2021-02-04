import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery1 = { "address": "Park Lane 38" }

mydoc1 = mycol.find(myquery1)

for x in mydoc1:
  print(x)

myquery2 = { "address": { "$gt": "S" } }

mydoc2 = mycol.find(myquery2)

for x in mydoc2:
  print(x)

myquery3 = { "address": { "$regex": "^S" } }

mydoc3 = mycol.find(myquery3)

for x in mydoc3:
  print(x)