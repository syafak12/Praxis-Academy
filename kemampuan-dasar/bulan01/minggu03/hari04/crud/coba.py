from http import client
import pymongo


# Ganti string uri dengan string koneksi penyebaran MongoDB Anda.
conn_str = "mongodb+srv://syafak12:<password>@cluster0.5a54x.mongodb.net/test"

# atur batas waktu koneksi 5 detik
client = pymongo.MongoClient(conn_str, serverSElectionTimeoutMS=5000)

try:
    print(client.server_info())
except Exception:
    print("cek")