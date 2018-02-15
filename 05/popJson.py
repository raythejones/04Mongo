import pymongo
import json

connection=pymongo.MongoClient("homer.stuy.edu")
db = connection['jonathanQ-jonesR-db']
collection = db['jonathanQ-jonesR-collection']




file = open("populationUSA.json","r")
data = file.read()

print(data)

collection.insert_one(data)

