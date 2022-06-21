from flask import Flask
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conn = Flask psycop