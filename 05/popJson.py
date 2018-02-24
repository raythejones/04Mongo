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

