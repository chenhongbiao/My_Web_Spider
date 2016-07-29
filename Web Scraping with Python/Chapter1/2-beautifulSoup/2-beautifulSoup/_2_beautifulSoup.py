from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
#print(html.read()) # get the whole HTML content of this page
print(html.read())
print("-------------------------------------------------")
bsObj = BeautifulSoup(html.read(),"html.parser")
print(bsObj)
#UserWarning: No parser was explicitly specified, so I'm using the best
#available HTML parser for this system ("html.parser"). This usually isn't a
#problem, but if you run this code on another system, or in a different
#virtual environment, it may use a different parser and behave differently.

#To get rid of this warning, change this:
#BeautifulSoup([your markup])
#to this:
#BeautifulSoup([your markup], "html.parser")
print("Let try to print its h1 if it's existed")
print(bsObj.h1)
#print(bsObj.html.h1) #something it work but something it say it don't have this attributes
#print(bsObj.body.h1)
#print(bsObj.html.body.h1)
#notice that h1 is in the two deep layer (html->body->h1)
#and above ways are okay to access h1 
