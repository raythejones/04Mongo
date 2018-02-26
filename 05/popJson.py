"""
Dataset Name: 1950 US population
Link: http://api.population.io/1.0/population/1950/United%20States/?format=json
Summary of import mechanism:
Get rid of beginning and ending brackets, then split along },{ for constructing dictionary entries

"""


import pymongo
import json

connection=pymongo.MongoClient("homer.stuy.edu")
db = connection['usStats']
collection = db['usStatsCollection']



file = open("populationUSA.json","r")
data = file.read()

#print(data)

#parse the data

#first remove the starting and ending [{ and }]
data = data[2:len(data)-2]

#split along }, {
data = data.split("}, {")



for index in data:
    dataDict = {}
    rowSplit = index.split(', ')
    for dataPair in rowSplit:
        colonIndex = dataPair.find(':')
        theKeyNoQuotes = dataPair[1:colonIndex-1]
        theValue = dataPair[colonIndex+2:len(dataPair)]
        theValue = theValue.strip('"')
        dataDict[theKeyNoQuotes]=theValue
    print dataDict
    collection.insert_one(dataDict)



#collection.insert_one(data)



def byMales(theMales):
	bData = collection.find({'males':theMales})
	for theObject in bData:
		print theObject['age']
        return bData
		
print byMales("1121000")

def byFemales(theFemales):
        bData = collection.find({'females':theFemales})
        for theObject in bData:
            print theObject['age']
        return bData

print byFemales("1119000")

def byMalesAndFemales(theMales,theFemales):
	bData = collection.find({'males':theMales,'females':theFemales})
        for theObject in bData:
            print theObject['age']
        return bData
		
print byMalesAndFemales("1158000","1147000")
print byMalesAndFemales('0','0')
