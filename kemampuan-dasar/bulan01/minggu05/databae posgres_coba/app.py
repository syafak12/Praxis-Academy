from codecs import namereplace_errors
from flask import Flask, jsonify, request, json
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(host="0.0.0.0", database="postgres", user="lorna", password="password")
curs = conn.cursor()

@app.route("/list", methods=["GET"])
def list():
    try:
        query = f"select * from lorna"
        curs.execute(query)
        result = curs.fetchall()
        print(result)
        return jsonify({
            "id": "aku sangat rindu",
            "title": 2
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