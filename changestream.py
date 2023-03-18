import pymongo
from bson.json_util import dumps
from dotenv import dotenv_values
config = dotenv_values(".env")

client = pymongo.MongoClient(config["DB_URI"])
db = client["famguy"]
collection = db["chars"]
change_stream = collection.watch()

for change in change_stream:
    print(dumps(change))
    print('')


"""

If there is this error:

    The $changeStream stage is only supported on replica sets

Then:

    1. Go to /etc/mongod.config 
    2. Add these two lines:
        
        replication:
          replSetName: rs1

          
Then, go to terminal and type:

    sudo systemctl restart mongod 

Then, go to terminal and type "mongosh", then:

    1. rs.initiate()
    2. rs.status()

DONE
          
"""
