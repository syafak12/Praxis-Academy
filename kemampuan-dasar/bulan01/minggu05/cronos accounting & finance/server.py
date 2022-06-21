from flask import Flask, jsonify, request, json
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(host="0.0.0.0", database="postgres", user="lorna", password="password")
curs = conn.cursor()

@app.route("/satu", methods=["GET"])
def satu():
    try:
        query = f"select * from features"
        curs.execute(query)
        result = curs.fetchall()
        # print(result)

        data = []
        for i in result:
            data.append({
                "id": i[0],
                "upload": i[1]
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
        upload = payload["upload"]
        query = f"insert into features (upload) values ('{upload}')"
        curs.execute(query)
        conn.commit()
        # result = curs.fetchall()
        # print(result)
        return jsonify({
            "message": "sukses",
            "data": upload
        })
    except Exception as e:
        return jsonify({
            "message": "Gagal memasukkan data"
        }), 400

if "__name__"=="__main__":
    app.run(host="0.0.0.0", port=8080)