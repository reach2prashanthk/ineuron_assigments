from pymongo.mongo_client import MongoClient
url = "mongodb+srv://prashaanth:1234@cluster0.aufa7mx.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(url)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

d={'name':'prashanth',
   'email':'kp@gmail.com',
   'surname':'pi'}

db1=client['mongootest']
coll=db1['test']
coll.insert_one(d)