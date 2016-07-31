import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "H:\SpiderPic"
baseUrl = "https://m.douban.com"

def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://"+source[11:]
    elif source.startswith("http://") or source.startswith("https://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://"+source
    else:
        url = baseUrl+"/"+source
    if url.endswith(".jpg"):
        return url
    else:
        return None
    #if baseUrl not in url:
       #return None

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.", "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory+path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)

    return path

html = urlopen("https://m.douban.com/photos/album/1627562414/")
bsObj = BeautifulSoup(html,"html.parser")
downloadList = bsObj.findAll("img")
filename="a"
for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)
        #urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
        filename = filename+"a"
        urlretrieve(fileUrl,"H:\SpiderPic\\"+filename+".jpg")