import json

allNodesList = []

myFile = open("RTD_POINTMap.html","r")

myText = []


for myLine in myFile:
    # Stop once we hit data.  Standard structure for all 
    if myLine[:29] == '<area shape="POLY" alt="Node:':
        myNodeName = myLine[30:].strip()

        myLine = myFile.next()
        myNodeType = myLine[11:].strip()
        
        # Advance through cost information lines
        myLine = myFile.next() # Marginal clearing price
        myLine = myFile.next() # Divider
        myLine = myFile.next() # Congestion
        myLine = myFile.next() # Cost LMP
        
        myLine = myFile.next() # This is the data we want
        
        # Latitude is found after the first double quote, and does not have a fixed length
        # Latitude is followed by '&longitude=' and then followed by the longitude
        # Longitude is not a fixed length, but is followed by another double quote
        # Following line should start with <area
        
        latitudeStart = myLine.find('"')
        latitudeEnd = myLine.find('&')
        latitude = myLine[latitudeStart+1:latitudeEnd].strip()
        
        longitudeStart = latitudeEnd + 11
        longitudeEnd = myLine.find('"',latitudeEnd)
        longitude = myLine[longitudeStart:longitudeEnd].strip()
        
        print 'Node name = ', myNodeName, '\tNode Type= ',myNodeType, '\tLatitude= ' , latitude , '\tLongitude= ', longitude
        
        myNodeDict = {'name':myNodeName, 'type':myNodeType,'latitude':latitude,'longitude':longitude}
        
        allNodesList.append(myNodeDict)

print 'Total number of nodes processed: ', len(allNodesList)

myOutput = open('RTD_PointMap_Nodes.json','write')
json.dump(allNodesList,myOutput)
myOutput.close()
myFile.close()