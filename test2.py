import pymongo


client=pymongo.mongoclient(mongodb+srv://rakesh:rakesh%@%123@rakesh.uowcycq.mongodb.net/?retryWrites=true&w=majority)
db=client.test
print(db)
d= {
    "name":"sudh",
   "email" : "sudh@inueron.ai",
   "surname":"kumar"
}
db1= client['mongotest']
coll=db1['test']
coll.insert_one(d)
