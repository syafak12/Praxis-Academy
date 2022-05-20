from multiprocessing import connection
from dotenv import find_dotenv, load_dotenv
from pymongo import MongoClient, MongoClient
import os
import pprint

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
print(password)
connection_string = f"mongodb+srv://coba3:{password}@cluster0.5fuoc.mongodb.net/test"
client = MongoClient(connection_string)