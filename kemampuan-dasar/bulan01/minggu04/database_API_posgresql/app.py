from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(host="localhost", database="postgres", user="lorna", password="password")

@app.route("/list", methods=["GET"])
def list():
    try:
        return jsonify({
            "id"
        })
    except Exception as e:
        print(e)

if "__name__"=="__main__":
    app.run(host="localhost", port=5432)