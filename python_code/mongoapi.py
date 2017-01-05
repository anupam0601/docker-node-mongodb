from pymongo import MongoClient
import datetime

"""client = MongoClient('mongodb://mongo:27017/')

# Set db connection
db = client['myproject']

Col = db.my_coll.find()

for i in Col:
	print i
"""

class MongoDefaults(object):
	""" Mongo DB basic methods """

	def __init__(self, client=None, db=None, collection=None, time_stamp=None):
		""" Constructor for db params """
		
		if client is None:
			client = MongoClient('mongodb://mongo:27017')
		
		if db is None:
			db = client['automation']
		
		if collection is None:
			collection = db['testlogs']

		if time_stamp is None:
			time_stamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

		self.db = db
		self.client = client
		self.collection = collection
		self.time_stamp = time_stamp

	def connect(self):
		try:
			db_connect = self.db
			print self.time_stamp
			if db_connect:
				print "connected"
				
			else:
				raise Exception("db connect error")
		except Exception as error:
			print error


if __name__ == '__main__':
	execdb = MongoDefaults()
	execdb.connect()