#import csv
#csvFile = open("test.csv", 'w+')
#try:
   #writer = csv.writer(csvFile)
    #writer.writerow(('number', 'number plus 2', 'number times 2'))
    #write a tuple as a row in the file
    #for i in range(10):
        #writer.writerow((i, i+2, i*2))
#finally:
    #csvFile.close()
    #finally like except but it would execute regardless whether 
    #the try statement have thrown an exception or not
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html,"html.parser")

#The main comparison table is currently the first table on the page
table = bsObj.findAll("table",{"class":"wikitable"})[0]
caption = table.find("caption")
#<caption>List of text editors</caption>
rows = table.findAll("tr")

csvFile = open("editors.csv", 'wt', newline='', encoding='utf-8')
writer = csv.writer(csvFile)
try:
	for row in rows:
		csvRow = []
		for cell in row.findAll(['td', 'th']):
            #find tag <td> or [th] under the  cell tag
			csvRow.append(cell.get_text())
		writer.writerow(csvRow)
        #write a Python list as a row into it
finally:
    csvFile.close()
