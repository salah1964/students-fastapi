#import statements
from pymongo import MongoClient

#create BD connection
#connection = MongoClient("mongodb://localhost:27017/test")
#connection = MongoClient()

#MongoDB Connection info
client = MongoClient("mongodb+srv://salah:palestinerafah1964@cluster0.5uof9.mongodb.net")
#Database
connection = client['school']