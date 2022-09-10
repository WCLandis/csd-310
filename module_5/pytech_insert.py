import pymongo
from pymongo import MongoClient
client= MongoClient("mongodb+srv://admin:admin@cluster0.rluwz.mongodb.net/?retryWrites=true&w=majority")
db= client["pytech"]
collection = db["students"]

post1 = {"_id": 1007, "First Name": "Bill", "Last Name": "Gates"}
post2 = {"_id": 1008, "First Name": "James", "Last Name": "Hetfield"}
post3 = {"_id": 1009, "First Name": "William", "Last Name": "Landis"}

collection.insert_many([post1, post2, post3])
