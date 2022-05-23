from flask import Flask

app = Flask(__name__)

@app.route('/profil')
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

@app.route('/profil_satu')
def datane_doni():
    data_satu = {
        "id": 1,
        "nama": "doni",
        "lahir": True,
        "kota": [
            "jogja",
            "sumber",
            "banyurowo"
        ],
    }

@app.route('/profil_dua')
def datane_adi():
    data_dua = {
        "id": 1,
        "nama": "adi",
        "lahir": True,
        "kota": [
            "pati",
            "tayu",
            "ndeso"
        ],
    }
    return ("profil", 
    "profil_satu", 
    "profil_dua")

    