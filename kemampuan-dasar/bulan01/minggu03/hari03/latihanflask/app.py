from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    data = {
        "id": 1,
        "nama": "syafak",
        "lahir": True,
        "kota": [
            "rembang",
            "sulang",
            "kapasan"
        ],
    }
    return data

    