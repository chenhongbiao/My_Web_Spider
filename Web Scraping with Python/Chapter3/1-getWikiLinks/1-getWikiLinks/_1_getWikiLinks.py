from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
#html = urlopen("https://chenhongbiao.github.io/")
bsObj = BeautifulSoup(html.read(),"html.parser")
#links = bsObj.findAll("a") #findAll() return a Python list of tags object 
#for link in links:
#    if "href" in link.attrs: #link is a tag object which attrs is a Python dict object
#        print(link.attrs["href"]) #href - Hypertext REFerence

for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
#((?!:).)* meaning that can be any character with any long but not ':' show in it
