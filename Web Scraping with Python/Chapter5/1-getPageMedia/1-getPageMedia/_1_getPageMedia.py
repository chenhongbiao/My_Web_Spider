from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

#http://space.bilibili.com/1950746/#!/index
#<div class="h-avatar">
#<img src="http://i2.hdslb.com/bfs/face/24032cad1ec7db242fda01061a4f8b3b998d170c.jpg" id="h-avatar" come-on-click-me!!="">
#</div>

#def getAvater(userid):
    #html = urlopen("http://space.bilibili.com/"+userid+"/#!/index")
    #bsObj = BeautifulSoup(html.read(),"html.parser")
    #imgtag = bsObj.find("img", id = "h-avater")
    #cannot find this tag due to bilibili use javascript to load all pic 
    #so you cannot find that tag in the raw html code
    #urlretrieve(imgtag["src"],userid+"avater")

#getAvater("1950746")

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")
imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
urlretrieve (imageLocation, "H:\SpiderPic\logo.jpg")