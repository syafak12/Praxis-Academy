from codecs import namereplace_errors
from flask import Flask, jsonify, request, json
import psycopg2

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(host="0.0.0.0", database="postgres", user="lorna", password="password")
curs = conn.cursor()

@app.route("/list", methods=["GET"])
def list():
    try:
        query = f"select * from lorna"
        curs.execute(query)
        result = curs.fetchall()
        print(result)

        data = []
        for i in result:
            data.append({
                "id": i[0],
                "nama": i[1],
                "nama_lengkap": i[2],
                "tanggal_lahir": i[3],
                "email": i[4]
            })
        return jsonify({
            "data": data
        })
    except Exception as e:
        print(e)

@app.route("/create", methods=["POST"])
def create():
    try:
        payload = json.loads(request.data)
        # print(payload)
        nama = payload["nama"]
        nama_lengkap = payload["nama_lengkap"]
        tanggal_lahir = payload["tanggal_lahir"]
        email = payload["email"]
        # print(nama, nama_lengkap, tanggal_lahir, email)
        query = f"insert into lorna(nama, nama_lengkap, tanggal_lahir, email) values ('{nama}', '{nama_lengkap}', '{tanggal_lahir}', '{email}')"
        curs.execute(query)
        conn.commit()
        # result = curs.fetchall()
        # print(result)
        return jsonify({
            "message": "sukses",
            "data": nama
        })
    except Exception as e:
        return jsonify({
            "message": "Gagal memasukkan data"
        }), 400

if "__name__"=="__main__":
    app.run(host="0.0.0.0", port=5000)