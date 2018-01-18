from pymongo import MongoClient
from bson import ObjectId
import sys, os, inspect
pathapp = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(pathapp + "/config")
import Environment as env

class MongoDb(object):
	
	def __init__(self):
		self.moConn = MongoClient('mongodb://' + env.MONGO_HOST + ':' + env.MONGO_PORT)
		self.dbname = self.moConn[env.MONGO_DB]
		
	def insert(self, collection, data):
		newRowId = self.dbname[collection].insert(data)
		print "New Row id: " + `newRowId`
		self.moConn.close()
