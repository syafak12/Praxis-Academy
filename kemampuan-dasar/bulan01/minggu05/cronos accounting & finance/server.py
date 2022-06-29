from distutils.command.config import config
import os
from flask import Flask, flash, jsonify, redirect, request, json, url_for
import psycopg2
from flask_cors import CORS

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
    
@app.route("/read", methods=["GET"])
def read():
    try:
        query = f"select * from content"
        curs.execute(query)
        result = curs.fetchall()
        data = []
        for i in result:
            data.append({
                "id": i[0],
                "id_features": i[1],
                "isi_content": i[2],
                "image": i[3]
            })
        return jsonify({
            "dtaa": data
        })
    except Exception as i:
        print (i)

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
    
    except Exception as e:
        return jsonify({
            "message": "Gagal memasukkan data",
            "error" : f"{e}"
        }), 400

@app.route("/upload", methods=["POST"])
def upload():
    try:
        payload = json.loads(request.data)
        id_features = payload["id_features"]
        isi_content = payload["isi_content"]
        image = payload["image"]
        query = f" insert into content (id_features), (isi_content), (image) values ('{id_features}'), ('{isi_content}'), ('{image}')"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "sukses memasukkan data content",
            "data": "id_features"
        }), 200

    except Exception as i:
        return jsonify({
            "message": "gagal memasukkan data content",
            "error": f"{i}"
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

@app.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    try:
        query = f"delete from content where id ={id}"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "sukses menghapus data"
        }), 200
    except Exception as i:
        return jsonify({
            "message": "gagal menghapus data",
            "detailMessage": f"{i}"
        }), 400

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

@app.route("/perbaharui/<id>", methods=["PUT"])
def perbaharui(id):
    try:
        payload = json.loads(request.data)
        id_features = payload["id_features"]
        isi_content = payload["isi_content"]
        image = payload["image"]
        query = f"update content (id_features), (isi_content), (image) values ('{id_features}'), ('{isi_content}'), ('{image}')"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "sukses memasukkan data content",
            "data": "id_features"
        }), 200
    except Exception as i:
        return jsonify({
            "message": "Gagal update data",
            "detailMessage": f"{i}"
        }), 400

if "__name__"=="__main__":
    app.run(host="0.0.0.0", port=8080)