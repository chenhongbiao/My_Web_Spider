from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html.read(),"html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
#return a list of tag which in this form <a herf = "/wiki/xxx">
#notice I didn't deal with exception

random.seed(datetime.datetime.now())
links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
    #the old links are go away, each time just pick up one link from it
    #so this is just a random traversal of Wikipedia
