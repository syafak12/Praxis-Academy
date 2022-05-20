import pymongo

db = pymongo.MongoClient("mongodb://cluster0.5fuoc.mongodb.net")

#database
dbku = db["blog"]
#collection
collectionku = dbku['artikel']

#data yang akan di insert
data = {}
data = [
    {"judul": "belajar ngoding python-mongodb"},
    {"penulis": "musyaffak"},
    {"kelebihan": "bergerak"},
    {"kekuatan": "ngantuks"},
    ]

# data diinsert
collectionku.insert_one(data)