import pymongo

db = pymongo.MongoClient("mongodb://localhost:27017")

#database
dbku = db["blog"]
#collection
collectionku = dbku['artikel']

#data yang akan di insert
data = {"judul": "belajar ngoding python-mongodb", "penulis": "musyaffak"}

# data diinsert
collectionku.insert_one(data)