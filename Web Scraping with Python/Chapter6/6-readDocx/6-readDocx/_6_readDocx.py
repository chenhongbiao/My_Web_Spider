from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile) #turn it into Bytes stream so can be unzipp (open a zip file)
document = ZipFile(wordFile)
#xml_content = document.read('document.xml') 
#it seems that zip create a xml file name like below in the memory
#you can see that in the debug windows
xml_content = document.read('word/document.xml')
    #return file bytes as a string for name
print(xml_content.decode('utf-8'))

wordObj = BeautifulSoup(xml_content.decode("utf-8"),"html.parser")
textStrings = wordObj.findAll("w:t")
for textElem in textStrings:
    print(textElem.text)
    #get_text()