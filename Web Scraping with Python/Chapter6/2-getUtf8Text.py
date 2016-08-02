from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://chenhongbiao.github.io/cn/2015/03/64bit-Assembly-Debug/")
bsObj = BeautifulSoup(html,"html.parser")
content = bsObj.find("article", {"class":"content"}).find("h3", id="为什么").get_text()
#<article class="content">
#content = bytes(content, "UTF-8")
#content = content.decode("UTF-8")
print(content)
#print(bsObj)
#print(bsObj.get_text())
