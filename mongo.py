import pymongo

connection=pymongo.MongoClient("homer.stuy.edu")
print(connection)

theTest = connection.test

print (theTest)

theRest = theTest.restaurants

print (theRest)

def byBorough(theBorough):
	bData = theRest.find({'borough':theBorough})
	for theObject in bData:
		print theObject['name']


byBorough('Brooklyn')
