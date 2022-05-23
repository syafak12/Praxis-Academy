# from multiprocessing import connection
# from dotenv import find_dotenv, load_dotenv
# from pymongo import MongoClient, MongoClient
# import os
# import pprint

# load_dotenv(find_dotenv())

# password = os.environ.get("MONGODB_PWD")
# print(password)
# connection_string = f"mongodb+srv://coba3:{password}@cluster0.5fuoc.mongodb.net/test"
# client = MongoClient(connection_string)
import pymongo 

Client = pymongo.MongoClient("Turusgede")
print(Client.list_database_names())

mydb = Client["mydb"]
mycol = mydb["Turuswetan"]

data = {'nama': 'syafak', 'usia': 22}
mycol.insert_one(data)
datalist = [{'nama': 'adi', 'usia': 25}, {'nama': 'uud', 'usia': 30}]
mycol.insert_many(datalist)

# melakukan looping dari database
mydb=Client["Turusgede"]
mycol = mydb['DtlCont']
for x in mycol.find({"jumlah anak":{"$gte": "3"}}):
  print(x)


mydb = Client["Turusgede"]
mycol = mydb['DtlCont']
for x in mycol.find():
  print(x)
