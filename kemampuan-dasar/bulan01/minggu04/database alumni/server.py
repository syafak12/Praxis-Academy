from flask import Flask, Response, request
import pymongo
import json
from bson.objectid import ObjectId
app = Flask(__name__)

try:
    mongo = pymongo.MOngoClient(
        host-"localhost",
        port=27017,
        serverSelectionTimeoutMS=1000
    )

    db = mongo.database alumni
    mongo.server_info()
    except:
        print("MAAF - tidak connect ke db")

#############
### membaca data (read)
############
@app.route("/read", methods=["GET"])
def get_some_users():
    try:
        data = list(db.data_alumni.find())
        for user in data:
            user["_id"] = str(user["__id"])