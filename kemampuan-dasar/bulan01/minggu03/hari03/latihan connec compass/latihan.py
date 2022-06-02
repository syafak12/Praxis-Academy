
from flask import Flask, Response
from flask_pymongo import PyMongo
import json

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/youtubedb"
mongo = PyMongo(app)

@app.route("/users", methods=["GET"])
def get_some_users():
    try:
        data = list(mongo.users.find())
        for user in data:
            user["_id"] = str(user["_id"])
        return Response(
            response= json.dumps(data),
            status=500,
            mimetype="application/json"
            )
    except Exception as ex:
        print(ex)
        return Response(response= json.dums({"message": "cannot read users"}), status=200, mimetype="application/json")

if __name__ == "__main__":
    app.run()
