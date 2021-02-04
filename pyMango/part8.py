import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Mountain 21" }

mycol.delete_one(myquery)

myquery1 = { "address": {"$regex": "^S"} }

x = mycol.delete_many(myquery1)

print(x.deleted_count, " documents deleted.")

y = mycol.delete_many({})

print(y.deleted_count, " documents deleted.")