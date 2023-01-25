import pymongo
client = pymongo.MongoClient("mongodb+srv://rakesh:rakesh@123.uowcycq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name":"sudh",
   "email" : "sudh@inueron.ai",
   "surname":"kumar",
}
d1= {
    "name":"sudh",
   "email" : "sudh@inueron.ai",
   "surname":"kumar",
}
d= {
    "name":"sudh",
   "email" : "sudh@inueron.ai",
   "surname":"kumar",
}coll.insert_one(d1 )
d= {
    "name":"sudh",
   "email" : "sudh@inueron.ai",
   "surname":"kumar",
}