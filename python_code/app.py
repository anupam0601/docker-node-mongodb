from pymongo import MongoClient
client = MongoClient('mongodb://mongo:27017/')

# Set db connection
db = client['myproject']

Col = db.my_coll.find()

for i in Col:
	print i