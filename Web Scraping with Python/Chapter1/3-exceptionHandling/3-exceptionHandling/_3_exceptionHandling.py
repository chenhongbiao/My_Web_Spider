from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        #The page is not found on the server - 404 (or there was some error in retrieving it)
        #urlopen() would throw HTTPError
        #But If the server is not found at all - let say, mistype the url, urlopen() return a None object
        #so the html you got is a None object
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"html.parser")
        title = bsObj.body.h1
        #if the tag you want is not existed, BeautifulSoup would return a None object
        #if you want to call something(like Attribute) above the None object, it will throw a Error
        #An AttributeError: 'xx' object has no attribute 'xx'
        #Always remember every tag may be not existed
    except AttributeError as e:
        return None
    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
#title = getTitle("http://www.chenhongbiao.github.com")
if title == None:
    print("Title could not be found")
else:
    print(title)

#Hei, guy. I encounter an error here
#if I connect the "God" wireless, it would occur the error 
#用户代码未处理 urllib.error.URLError Message: <urlopen error [Errno 11001] getaddrinfo failed>
#but befor 1 hour ago, it work well. Now, it crash! =- =
#but if I change the wireless "HP", it would be fine. Why? En...
#At least I know there is nothing wrong in my code and my machine. :) 