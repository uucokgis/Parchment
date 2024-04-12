from pymongo import MongoClient


__client = MongoClient('localhost', 27017)
db = __client.parsomen

