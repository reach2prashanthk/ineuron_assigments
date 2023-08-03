
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://prashanth:1234@prashanth.pynnq4g.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

d={
    'name':'prashanth',
    'email':'k@gmail.com',
    'surname':'kp'
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)