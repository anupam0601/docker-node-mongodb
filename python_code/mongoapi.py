from pymongo import MongoClient
import datetime
from json_parser import data
from json_logger import Logger


class MongoApi(object):
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
        """ Mongo DB connect """
        try:
            db_connect = self.collection
            print self.time_stamp
            if db_connect:
                print "Connected to db coll\
                       Please look into DB for status of test logs"

            else:
                raise Exception("db connect error")
        except Exception as error:
            print error

    # def log_insert(self, mongo_data):
    # 	""" log insert into testlogs collection """
    # 	try:
    # 		post_id = self.collection.insert(mongo_data)
    # 		return post_id
    # 	except Exception as error:
    # 		print error

    # def log_update(self, log_field):

if __name__ == '__main__':
    execdb = MongoApi()
    # execdb.connect()
    print execdb.log_insert(mongo_data=data["log_stat"])
