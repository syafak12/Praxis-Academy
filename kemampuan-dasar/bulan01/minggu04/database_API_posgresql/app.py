from urllib import response
from flask import Flask, render_template, Response, request, redirect, url_for, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import json

app = Flask(__name__)

try:
    DB_HOST = "localhost"
    DB_NAME = "postgres"
    DB_USER = "lorna"
    DB_PASS = "password"
 
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
except:
    print("ERROR - tidak bisa connect ke posgreSQL")

@app.route('/')
def Index():
    # return render_template('index.html')
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM hasil_penjualan"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()
    return render_template('index.html', list_users = list_users)    
     
##############
# membaca data (read)
#############
@app.route("/read", methods=["GET"])
def get_some_users():
    try:
        data = list(db.masuk_data.find())
        for user in data:
            user["_id"] = str(user["_id"])
        return Response(
            response= json.dumps(data),
            status=500,
            mimetype="aplication/json"
        )

    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({"message": "tidak bisa membaca users"}), status=500, mimetype="aplication/json")

#############
## membuat data (creat)
############

@app.route("/creat", methods=["POST"])
def create_user():
    try:
        payload = json.loads(request.data)
        # user = {
        #     'Nama': request.values["Nama"],
        #     'Daerah': request.values["Daerah"],
        #     'tahunMasuk': request.values["tahunMasuk"],
        #     'tahunKeluar': request.values["tahunKeluar"],
        #     'NoHp': request.values["NoHp"],
        #     'Email': request.values["Email"]
            # }
        # print(payload)
        dbResponse = db.masuk_data.insert_one(payload)
        print(dbResponse.inserted_id)
        return Response(
            response=json.dumps(
                {"message": "user sudah terbaca",
                "id":f"{dbResponse.inserted_id}"}),
            status=200,
            mimetype="aplication/json")
            
    except Exception as ex:
        print("*******")
        print(ex)
        print("*******")

############
# memperbaharui data (update)
###########
@app.route("/update/<id>", methods=["PATCH"])
def update_user(id):
    try:
        dbResponse = db.masuk_data.insert_one(
            {"_id": ObjectId(id)},
            {"$set":{'Nama': request.form["Nama"]}},
            {"$set":{'Daerah': request.form["Daerah"]}},
            {"$set":{'tahunMasuk': request.form["tahunMasuk"]}},
            {"$set":{'tahunKeluar': request.form["tahunKeluar"]}},
            {"$set":{'NohHp': request.form["NoHp"]}},
            {"$set":{'Email': request.form["Email"]}}
        )
        if dbResponse.modified_count == 1:
            return Response(
                response= json.dums(
                    {"message": "update berhasil"}),
                status=200,
                mimetype="aplication/json"
            )
        return Response(
            response= json.dums(
                {"message": "tidak bisa update"}),
            status=200,
            mimetype="aplication/json"
        )
    except Exception as ex:
        print("******")
        print(ex)
        print("*****")
        return Response(
            response= json.dums(
                {"message": "maaf ya, tidak bisa update"}),
            status=500,
            mimetype="aplication/json"
        )
#######
# menghapus data (delete)
######
@app.route("/delete/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        dbResponse = db.data_masuk.delete_one({"_id":ObjectId(id)}),
        if dbResponse.deleted_count == 1:
            return Response(
                response= json.dums(
                    {"message": "berhasil di delete", "id":f"{id}"}),
                status=200,
                mimetype="aplication/json"
            )
    

    except Exception as ex:
        print("*****")
        print(ex)
        print("*****")
        return Response(
            response= json.dums(
                {"message": "maaf ya, tidak bisa delete user"}),
            status=500,
            mimetype="aplication/json"
        )

###########
if __name__ == "__main__":
    app.run(debug=True)