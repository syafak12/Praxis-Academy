from multiprocessing import connection
from dotenv import find_dotenv, load_dotenv
from pymongo import MOngoClient, MongoClient
import os
import pprint

load_dotenv(find_dotenv())

pasword = os.eviron.get("MONGODB_PWD")
print(password)
connection_string = f"mongodb+srv://syafak12":{pasword}@mongodb+srv://turusgede:<password>@cluster0.kefff.mongodb.net/test
Client = MongoClient(Connection_string)