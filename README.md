# python-changestream

### 1. Start the Change Stream Listener:
    
     python3 changestream.py
     
This file will listen to changes in the `chars` collection in the `famguy` database.
     
### 2. Test by inserting a document to that collection

    python3 changestream-client.py
    
    
    
## Very Common Error
There's a very common error that people get when they run a MongoDB ChangeSteam file if their database is on localhost. The error might look like this: 

    The $changeStream stage is only supported on replica sets
    
If you get this error, follow these steps:

  ### 1. Go to `/etc/mongod.config` and add these two lines:
    
    replication:
      replSetName: rs1
      
  ### 2. Go to terminal and type these commands individually (per line):
  
    sudo systemctl restart mongod 
    
    mongosh
    
    rs.initiate()
    
    rs.status()
    
 Now, you should be good to go
