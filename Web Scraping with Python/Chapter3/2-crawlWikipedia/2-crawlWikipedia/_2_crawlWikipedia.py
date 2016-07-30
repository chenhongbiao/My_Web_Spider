from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id ="mw-content-text").findAll("p")[0].get_text())
        #! 'gbk' codec can't encode character '\xa0' in position 464: illegal multibyte sequence
        #the page is encode by utf-8 and we decode it correctly but [the win8 terminal "print"] want to show you as gbk encode
        #some utf-8 decode 10 cannot transfer into gbk code, so throw the exception

        #so... Let's show it as utf-8? well, it's hard to do this in vs 2015, so I change my console as "cmd", run .py in cmd =-=
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        #Hey, there is page href that it didn't cover 
        #<a href="//shop.wikimedia.org" title="Visit the Wikipedia store">Wikipedia store</a>
        #<a href="https://donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&amp;utm_medium=sidebar&amp;utm_campaign=C13_en.wikipedia.org&amp;uselang=en" title="Support us">Donate to Wikipedia</a>
        #a good web scraper can be built in a good html website...
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")