from distutils.command.config import config
import os
from flask import Flask, flash, jsonify, redirect, request, json, url_for
import psycopg2
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(host="0.0.0.0", database="menu", user="menu", password="12345")
curs = conn.cursor()

@app.route("/baca", methods=["GET"])
def baca():
    try:
        query = f"select * from features"
        curs.execute(query)
        result = curs.fetchall()
        # print(result)

        data = []
        for i in result:
            data.append({
                "id": i[0],
                "nama": i[1]
            })
        return jsonify({
            "data": data
        })
    except Exception as e:
        print(e)
    
@app.route("/membuat", methods=["POST"])
def create():
    try:
        # file = request.files["media"]
        # print(file)
        payload = json.loads(request.data)
        # print(payload)
        nama = payload["nama"]
        query = f"insert into features (nama) values ('{nama}')"
        curs.execute(query)
        conn.commit()
        # result = curs.fetchall()
        # print(result)
        return jsonify({
            "message": "sukses membuat data",
            "data": "nama"
        })
    #     payload = json.loads(request.data)
    #     # print(payload)

    #     upload = payload["upload"]
    #     query = f"insert into features"
    #     query = 'insert into features (upload) values ("%s")'%("upload")
    #     query = f"into features set upload=('{upload}')"
    #     print(query)
    #     curs.execute(query)
    #     conn.commit()
    #     conn.close
    #     curs.close
    #     result = curs.fetchall()
    #     print(result)
    #     return jsonify({
    #         "message": "sukses",
    #         "data": []
    #     })
    except Exception as e:
        return jsonify({
            "message": "Gagal memasukkan data",
            "error" : f"{e}"
        }), 400
@app.route("/hapus/<id_menu>", methods=["DELETE"])
def hapus(id_menu):
    try:
        # print(id)
        query = f"delete from features where id_menu ={id_menu}"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message":"sukses menghapus data",
        }),200
    except Exception as e:
        return jsonify({
            "message": "Gagal menghapus data",
            "detailMessage":f"{e}"
        }),400

@app.route("/update/<id_menu>", methods=["PUT"])
def update(id_menu):
    try:
        payload = json.loads(request.data)
        print(payload)
        nama = payload["nama"]

        query = f"update features set nama=('{nama}') where id_menu=({id_menu})"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "sukses update data"
        })
    except Exception as e:
        return jsonify({
            "message": "Gagal update data",
            "detailMessage": f"{e}"
        }), 400
# @app.route

if "__name__"=="__main__":
    app.run(host="0.0.0.0", port=8080)