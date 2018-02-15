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
        return bData

def byZip(theZip):
        zData = theRest.find({'address.zipcode':theZip})
        for theObject in zData:
            print theObject['name']
        return zData

def byZipAndGrade(theZip,theGrade):
    zgData = theRest.find({'address.zipcode':theZip,'grades.grade':theGrade})
    for theObject in zgData:
        print theObject
    return zgData


def byZipAndLowerScores(theZip,theScore):
    zlsData = theRest.find({
        'address.zipcode':theZip,
        'grades.score':{'$lt':theScore}
        })
    for theObject in zlsData:
        print theObject['name']
    return theObject

def discoverZipCodesInBorough(theBorough):
    zData = theRest.find({'borough':theBorough})
    retArray = []
    for theObject in zData:
        isInArray = False
        itemToAdd = theObject['address']['zipcode']
        for item in retArray:
            if (item == itemToAdd):
                isInArray = True
        if (isInArray == False):    
            retArray.append(theObject['address']['zipcode'])
    print retArray

print('------Borough Brooklyn  ----- ')
byBorough('Brooklyn')
print('-----ZIP 11209----')
byZip('11209')
print('-----Zip 11209 Grade A----')
byZipAndGrade('11209','A')
print('-----Zip 11209 Score 6 ----')
byZipAndLowerScores('11209',5)
print('----zipcodes in Brooklyn-----')
discoverZipCodesInBorough('Brooklyn')
