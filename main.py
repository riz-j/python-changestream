import os
import pymongo
from dotenv import dotenv_values
config = dotenv_values(".env")

client = pymongo.MongoClient(config["DB_URI"])
db = client["famguy"]
collection = db["chars"]

cursor = collection.find({})

for document in cursor:
    print(document)
