import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }
myquery1 = { "address": { "$regex": "^S" } }
newvalues1 = { "$set": { "name": "Minnie" } }

mycol.update_one(myquery, newvalues)
x = mycol.update_many(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)
print(x.modified_count, "documents updated.")