import os
import pymongo
from model_character import Character
from dotenv import dotenv_values
config = dotenv_values(".env")

client = pymongo.MongoClient(config["DB_URI"])
db = client["famguy"]
collection = db["chars"]


_NewCharacter1 = Character("Peter Griffin", "Main character", "Quahog")
_NewCharacter2 = Character("Joe Swanson", "Neighbor", "Quahog")
_NewCharacter3 = Character("Cleveland Brown", "Neighbor", "Quahog")
_NewCharacter4 = Character("Chris Griffin", "Main character", "Quahog")
collection.insert_many([_NewCharacter1.to_dict(),
                       _NewCharacter2.to_dict(),
                       _NewCharacter3.to_dict(),
                       _NewCharacter4.to_dict()])
