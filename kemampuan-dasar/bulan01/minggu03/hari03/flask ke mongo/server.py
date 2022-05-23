from flask import Flask
import pymongo
app = Flask(__name__)

####################
@app.route("/users", methods=["POST"])
def create_user():  

try:
    mongo = pymongo.MOngoClient(
        host="localhost",
        port=27017,
        serverSElectionTimeoutMS = 1000
        )
        db = mongo.company
        mongo.server_info()   #memicu pengecualian jika tidak dapat terhubung ke db
except:
    print("ERROR - Cannot")
####################
if __name__== "__main__" :
    app.run(port=80, debug=True)