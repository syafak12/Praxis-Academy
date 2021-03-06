from flask import Flask, Response
import pymongo
app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimoutMS = 1000  
    )
    db = mongo.data_alumni
    mongo.server_info() # memicu pengecualian jika tidak bisa ke db
except:
    print ("ERROR - Cannot connect to db")
#################
@app.route('/users', methods=["POST"])
def create_user():
    try:
        user = {"name": "A", "lastName": "AA"}
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)
        # for attr in dir(dbResponse):
        #     print(attr)
        return Response(
            response= {"message": "user created", "id":f"{dbResponse.inserted_id}"},
            status=200,
            mimetype="application/json"
            )
    except Exception as ex:
        print("**********")
        print(ex)
        print("**********")


if __name__ == "__main__":
    app.run()