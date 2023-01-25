import pymongo
client = pymongo.MongoClient("mongodb+srv://rakesh:rakesh@123.uowcycq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name":"sudh",
   "email" : "sudh@inueron.ai",
   "surname":"kumar",
}
db1=client['mongotest']
coll= db1['test']
coll.insert_one(d )
