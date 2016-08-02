from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode("ascii")
dataFile = StringIO(data) #make it look like a file stream so the csv library would like to deal with it
#csvReader = csv.reader(dataFile)
#print(csvReader)
#print("-----------------------------")
#for row in csvReader:
#    print(row)
#   print("The ablum "+row[0]+"was realeased in "+str(row[1]))

dictReader = csv.DictReader(dataFile)
print(dictReader.fieldnames)
#this take the first pair as the fieldname
for row in dictReader:
    print(row)

dataFile.close() 