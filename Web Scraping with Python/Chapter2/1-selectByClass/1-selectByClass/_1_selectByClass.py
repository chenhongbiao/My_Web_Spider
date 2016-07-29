from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
#print(html.read()) #print the raw html
# strange... once use this statement, the print(bsObj) didn't work.
bsObj = BeautifulSoup(html.read(),"html.parser")
#print(bsObj) #print the tree structure html~

colorList = bsObj.findAll("span", {"class":"green", "class":"red"})
#the following function would return both the green and red span tags in the HTML document:
for content in colorList:
    print(content.get_text())
#strange... it only occur the first one match, not the expected both*

nameList = bsObj.findAll("span",{"class":"green"})
for name in nameList:
    #print("name.get_next(): ", name.get_text())
    print("name: ", name) 

wordList = bsObj.findAll("span",{"class":"red"})
for word in wordList:
    print(word.get_text())

heList = bsObj.findAll(text = "the prince")
#the text should all* in the tags <span class="green">the prince</span>
print(len(heList))

#allText = bsObj.findAll(id="text")
#print(allText[0].get_text())