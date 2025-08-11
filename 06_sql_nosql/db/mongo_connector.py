from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
mongo_db = client['flask_mvc_demo']
mongo_users = mongo_db['users']
