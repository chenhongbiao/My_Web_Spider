from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(),"html.parser")

for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)

print("------------------------------------------------------------------")

for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
#get rid of the first row of the table - the title of the table 
#.tr.next_siblings

#yeah. we also have .next_sibling and .previous_sibling which are only return one tag* instead of a list

print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
#yeah, we also have .parents (so you can say hello to your father's father's father...)