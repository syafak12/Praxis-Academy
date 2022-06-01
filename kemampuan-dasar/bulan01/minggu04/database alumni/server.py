from crypt import methods
from flask import Flask, Response, request
import pymongo
import json
from bson.objectid import ObjectId
app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimoutMS = 1000  
    )
    db = mongo.company
    mongo.server_info() # memicu pengecualian jika tidak bisa ke db
except:
    print ("ERROR - Cannot connect to db")
####################
@app.route("/users", methods=["GET"])
def get_some_users():
    try:
        data = list(db.users.find())
        for user in data:
            user["_id"] = str(user["_id"])
        return Response(
            response= json.dumps([{"id":1}], [{"id":2}]),
            status=200,
            mimetype="application/json"
            )
    except Exception as ex:
        print(ex)
        return Response(response= json.dums({"message": "cannot read users"}), status=200, mimetype="application/json")

####################
@app.route('/users', methods=["POST"])
def create_user():
    try:
        user = {
            "name":request.form["name"], 
            "lastName":request.form["lastName"]
            }
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)
        # for attr in dir(dbResponse):
        #     print(attr)
        return Response(
            response= json.dums(
                {"message": "user created", 
                "id":f"{dbResponse.inserted_id}" 
                }),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print("********")
        print(ex)
        print("********")
###################
@app.route("/users/<id>", methods["PATCH"])
def update_user(id):
    try:
        dbResponse = db.users.update_one(
            {"_id":ObjectId(id)},
            {"$set":{"name":request.from["name"]}}
        )
        # for attr ini dir(dbRensponse):
        #     print(f"*****{attr}*****")
        if dbResponse.modified_count == 1:
            return Response(
            response= json.dums(
                {"message": "user updated"}),
            status=200,
            mimetype="application/json"
        )
        return Response(
            response= json.dums(
                {"message": "nothing to update"}),
            status=200,
            mimetype="application/json"
        )
    except Exception as ex:
        print("******************")
        print(ex)
        print("******************")
        return Response(
            response= json.dums(
                {"message": "sorry cannot update user"}),
            status=500,
            mimetype="application/json"
        )
###################
@app.route("/users/<id>", methods: ["DELETE"])
def delete_user(id):
    try:
        dbResponse = db.users.delete_one({"_id":ObjectId(id)})
        if dbResponse.deleted_count == 1:
            return Response(response= json.dums({"message": "cannot delete user", "id":f"{id}"}), status=200, mimetype="application/json")
        return Response(response= json.dums({"message": "cannot delete user", "id":f"{id}"}), status=200, mimetype="application/json")
    except Exception as ex:
        print("******")
        print(ex)
        print("******")
        

###################


if __name__ == "__main__":
    app.run()