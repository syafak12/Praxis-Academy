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
        file = request.files["media"]
        print(file)
        # payload = json.loads(request.data)
        # # print(payload)
        # upload = payload["upload"]
        # query = f"insert into features (upload) values ('{upload}')"
        # curs.execute(query)
        # conn.commit()
        # result = curs.fetchall()
        # print(result)
        return jsonify({
            "message": "sukses",
            "data": "upload"
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
@app.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    try:
        # print(id)
        query = f"delete from features a where a.id={id}"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "sukses",
        })
    except Exception as e:
        return jsonify({
            "message": "Gagal menghapus data",
            "detailMessage": f"{e}"
        }), 400

@app.route("/update/<id>", methods=["PUT"])
def update(id):
    try:
        payload = json.loads(request.data)
        print(payload)
        upload = payload["upload"]

        query = f"update features set upload=('{upload}') where id=({id})"
        curs.execute(query)
        conn.commit()
        return jsonify({
            "message": "sukses"
        })
    except Exception as e:
        return jsonify({
            "message": "Gagal update data",
            "detailMessage": f"{e}"
        }), 400
# @app.route

if "__name__"=="__main__":
    app.run(host="0.0.0.0", port=8080)