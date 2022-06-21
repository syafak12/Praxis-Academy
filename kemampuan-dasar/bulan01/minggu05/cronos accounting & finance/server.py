from flask import Flask, jsonify, request, json
import psycopg2
from Flask_cors import CORS

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(host="0.0.0.0", database="postgres", user="features", password="password")
curs = conn.cursor()

@app.route("/features/satu", methods=["GET"])
def satu():
    try:
        query = f"select * from features"
        curs.execute(query)
        result = curs.fetchall()
        print(result)

        data = []
        for i in result:
            data.append({
                "upload": i[0]
            })
        return jsonify({
            "data": data
        })
    except Exception as e:
        print(e)

if "__name__"=="__main__":
    app.run(host="0.0.0.0", port=5000)