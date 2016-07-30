from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(),"html.parser")
images = bsObj.findAll("img",{"src":re.compile("\.\./img/gifts/img[1-9]\.jpg")})
#images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
#the return are the tags object in bs4
#bsObj can be seem as the root tag of the page - document
for image in images:
    print(image["src"])

#../img/gifts/img1.jpg